from enum import Enum


class ClusterCreateAttributeTagAgent(str, Enum):
    ALL_AGENTS = "all-agents"
    CMK_AGENT = "cmk-agent"
    NO_AGENT = "no-agent"
    SPECIAL_AGENTS = "special-agents"

    def __str__(self) -> str:
        return str(self.value)
