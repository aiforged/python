from enum import IntEnum


class AIForgedDALDocumentStatus(IntEnum):
    VALUE_0 = 0
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_81 = 81
    VALUE_90 = 90
    VALUE_98 = 98
    VALUE_99 = 99
    VALUE_103 = 103
    VALUE_108 = 108
    VALUE_109 = 109
    VALUE_110 = 110
    VALUE_190 = 190

    def __str__(self) -> str:
        return str(self.value)
