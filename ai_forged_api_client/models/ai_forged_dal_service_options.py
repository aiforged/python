from enum import IntEnum


class AIForgedDALServiceOptions(IntEnum):
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
    VALUE_2048 = 2048
    VALUE_4096 = 4096
    VALUE_8192 = 8192
    VALUE_16384 = 16384
    VALUE_32768 = 32768
    VALUE_65536 = 65536
    VALUE_131072 = 131072
    VALUE_262144 = 262144
    VALUE_524288 = 524288
    VALUE_1048576 = 1048576
    VALUE_2097152 = 2097152
    VALUE_4194304 = 4194304

    def __str__(self) -> str:
        return str(self.value)
