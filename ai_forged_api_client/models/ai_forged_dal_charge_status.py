from enum import IntEnum


class AIForgedDALChargeStatus(IntEnum):
    VALUE_0 = 0
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
