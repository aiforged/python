from enum import IntEnum


class AIForgedDALParameterDefinitionCategory(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_40 = 40

    def __str__(self) -> str:
        return str(self.value)
