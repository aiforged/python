from enum import IntEnum


class AIForgedDALUserGroupStatus(IntEnum):
    VALUE_0 = 0
    VALUE_99 = 99

    def __str__(self) -> str:
        return str(self.value)
