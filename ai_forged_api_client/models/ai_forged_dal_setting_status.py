from enum import IntEnum


class AIForgedDALSettingStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
