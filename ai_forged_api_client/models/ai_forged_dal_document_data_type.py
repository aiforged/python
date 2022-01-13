from enum import IntEnum


class AIForgedDALDocumentDataType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_10 = 10
    VALUE_11 = 11

    def __str__(self) -> str:
        return str(self.value)
