from enum import IntEnum


class AIForgedDALOptionStatusFlags(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_128 = 128
    VALUE_256 = 256
    VALUE_512 = 512
    VALUE_1024 = 1024

    def __str__(self) -> str:
        return str(self.value)
