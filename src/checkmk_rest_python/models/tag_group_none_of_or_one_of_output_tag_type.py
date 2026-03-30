from enum import Enum


class TagGroupNoneOfOrOneOfOutputTagType(str, Enum):
    AUX_TAG = "aux_tag"
    TAG_GROUP = "tag_group"

    def __str__(self) -> str:
        return str(self.value)
