from enum import IntEnum


class AIForgedDALPaymentStatus(IntEnum):
    VALUE_0 = 0
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_20 = 20
    VALUE_30 = 30
    VALUE_40 = 40
    VALUE_50 = 50
    VALUE_60 = 60
    VALUE_70 = 70
    VALUE_90 = 90
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
