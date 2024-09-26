"""Constants for the Rehau Neasmart 2.0 integration."""

DOMAIN = "rehau_nea_smart"
BINARY_STATUSES = {
    0: "Off",
    1: "On"
}

PRESENCE_STATES = {
    True: "Present",
    False: "Not Present"
}

PRESET_STATES_MAPPING = {
    "Пользовательский": 0,
    "Принудительно Авто": 4,
    "Принудительно Обычный": 1,
    "Принудительно Экономичный": 2,
    "Принудительно Режим ожидания": 3,
    "Принудительно Вечерина": 5,
    "Принудительно Отпуск": 6
}
PRESET_STATES_MAPPING_REVERSE = {v: k for k, v in PRESET_STATES_MAPPING.items()}

PRESET_STATES_CLIMATE_MAPPING = {
    "Авто": 4,
    "Обычный": 1,
    "Экономичный": 2,
    "Режим ожидания": 3,
    "Вечерина": 5,
    "Отпуск": 6
}
PRESET_STATES_CLIMATE_MAPPING_REVERSE = {v: k for k, v in PRESET_STATES_MAPPING.items()}

PRESET_CLIMATE_MODES_MAPPING = {
    "Пользовательский": 0,
    "Принудительно Авто": 1,
    "Принудительно Отопление": 2,
    "Принудительно Охлаждение": 3,
    "Принудительно Ручной режим отопленияв": 4,
    "Принудительно Ручной режим охлаждения": 5
}
PRESET_CLIMATE_MODES_MAPPING_REVERSE = {v: k for k, v in PRESET_CLIMATE_MODES_MAPPING.items()}
