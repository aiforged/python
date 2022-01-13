from enum import IntEnum


class AIForgedDALUsageType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_10 = 10
    VALUE_90 = 90
    VALUE_98 = 98
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
