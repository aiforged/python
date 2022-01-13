from enum import IntEnum


class AIForgedDALContactStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_90 = 90

    def __str__(self) -> str:
        return str(self.value)
