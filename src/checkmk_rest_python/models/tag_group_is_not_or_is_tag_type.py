from enum import Enum


class TagGroupIsNotOrIsTagType(str, Enum):
    TAG_GROUP = "tag_group"

    def __str__(self) -> str:
        return str(self.value)
