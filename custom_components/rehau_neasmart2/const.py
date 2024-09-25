"""Constants for the Rehau Neasmart 2.0 integration."""

DOMAIN = "rehau_neasmart2"
BINARY_STATUSES = {
    0: "Off",
    1: "On"
}
PRESENCE_STATES = {
    True: "Present",
    False: "Not Present"
}
PRESET_STATES_MAPPING = {
    "Обычный": 1,
    "Экономичный": 2,
    "Режим ожидания": 3,
    "Авто": 4,
    "Вечерина": 5,
    "Отпуск": 6
}
PRESET_STATES_MAPPING_REVERSE = {v: k for k, v in PRESET_STATES_MAPPING.items()}
PRESET_CLIMATE_MODES_MAPPING = {
    "Авто": 1,
    "Отопление": 2,
    "Охлаждение": 3,
    "Ручной режим отопленияв": 4,
    "Ручной режим охлаждения": 5
}
PRESET_CLIMATE_MODES_MAPPING_REVERSE = {v: k for k, v in PRESET_CLIMATE_MODES_MAPPING.items()}
