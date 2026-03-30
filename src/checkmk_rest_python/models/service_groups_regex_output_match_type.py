from enum import Enum


class ServiceGroupsRegexOutputMatchType(str, Enum):
    MATCH_ALIAS = "match_alias"
    MATCH_ID = "match_id"

    def __str__(self) -> str:
        return str(self.value)
