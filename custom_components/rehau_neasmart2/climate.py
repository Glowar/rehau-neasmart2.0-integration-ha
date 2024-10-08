from datetime import timedelta

SCAN_INTERVAL = timedelta(seconds=5)

import logging

import async_timeout

from .const import DOMAIN, PRESET_STATES_CLIMATE_MAPPING, PRESET_STATES_CLIMATE_MAPPING_REVERSE
from homeassistant.components.climate import ClimateEntity, ClimateEntityFeature, HVACMode
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.const import ATTR_TEMPERATURE

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add sensors for passed config_entry in HA."""
    hub = hass.data[DOMAIN][config_entry.entry_id]
    devices = [RehauNeasmart2ZoneClimateEntity(k) for k in hub.zones]

    if devices:
        async_add_entities(devices)


class RehauNeasmart2GenericClimateEntity(ClimateEntity, RestoreEntity):
    _attr_has_entity_name = False
    _attr_temperature_unit = UnitOfTemperature.CELSIUS

    def __init__(self, device):
        self._device = device
        self._state = None

    @property
    def device_info(self):
        return DeviceInfo(
            identifiers={(DOMAIN, self._device.id)},
            name=self._device.name,
            manufacturer=self._device.manufacturer,
            model=self._device.model,
        )

    @property
    def available(self) -> bool:
        return self._device.hub.online


class RehauNeasmart2ZoneClimateEntity(RehauNeasmart2GenericClimateEntity):
    def __init__(self, device):
        super().__init__(device)
        self._attr_unique_id = f"{self._device.id}_thermostat"
        self._attr_name = f"{self._device.name} Thermostat"
        self._attr_supported_features |= ClimateEntityFeature.PRESET_MODE
        self._attr_supported_features |= ClimateEntityFeature.TARGET_TEMPERATURE
        self._attr_hvac_modes = [HVACMode.AUTO]
        self._attr_hvac_mode = HVACMode.AUTO

        self._attr_preset_mode = None
        self._attr_preset_modes = list(PRESET_STATES_CLIMATE_MAPPING.keys())
        self._attr_current_humidity = None
        self._attr_current_temperature = None
        self._attr_target_temperature = None
        self._attr_max_temp = 26

    async def async_update(self) -> None:
        zone_data = await self._device.get_zone_data()
        if zone_data is not None and \
                zone_data.get("state") is not None and \
                zone_data.get("relative_humidity") is not None and \
                zone_data.get("temperature") is not None and \
                zone_data.get("setpoint") is not None:
            self._attr_preset_mode = PRESET_STATES_CLIMATE_MAPPING_REVERSE[zone_data["state"]]
            self._attr_current_humidity = zone_data["relative_humidity"]
            self._attr_current_temperature = zone_data["temperature"]
            self._attr_target_temperature = zone_data["setpoint"]
        else:
            _LOGGER.error(f"Error updating {self._attr_unique_id} thermostat")

    async def async_set_preset_mode(self, preset_mode: str):
        if not await self._device.set_zone_state(PRESET_STATES_CLIMATE_MAPPING[preset_mode]):
            _LOGGER.error(f"Error setting preset mode for {self._attr_unique_id} thermostat")

    async def async_set_temperature(self, **kwargs):
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is None:
            return
        if not await self._device.set_zone_setpoint(temperature):
            _LOGGER.error(f"Error setting temperature setpoint for {self._attr_unique_id} thermostat")
