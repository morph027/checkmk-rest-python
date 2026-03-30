from enum import Enum


class LDAPUsersSearchScope(str, Enum):
    SEARCH_ALL_ONE_LEVEL_BELOW_BASE_DN = "search_all_one_level_below_base_dn"
    SEARCH_ONLY_BASE_DN_ENTRY = "search_only_base_dn_entry"
    SEARCH_WHOLE_SUBTREE = "search_whole_subtree"

    def __str__(self) -> str:
        return str(self.value)
