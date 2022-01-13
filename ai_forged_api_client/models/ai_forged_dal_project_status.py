from enum import IntEnum


class AIForgedDALProjectStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_20 = 20
    VALUE_90 = 90
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
