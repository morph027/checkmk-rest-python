from enum import Enum


class AuxTagTagType(str, Enum):
    AUX_TAG = "aux_tag"

    def __str__(self) -> str:
        return str(self.value)
