from enum import Enum


class UpdateDiscoveryPhaseTargetPhase(str, Enum):
    ACTIVE = "active"
    CHANGED = "changed"
    CLUSTERED_IGNORED = "clustered_ignored"
    CLUSTERED_MONITORED = "clustered_monitored"
    CLUSTERED_UNDECIDED = "clustered_undecided"
    CLUSTERED_VANISHED = "clustered_vanished"
    CUSTOM = "custom"
    IGNORED = "ignored"
    IGNORED_ACTIVE = "ignored_active"
    IGNORED_CUSTOM = "ignored_custom"
    LEGACY = "legacy"
    LEGACY_IGNORED = "legacy_ignored"
    MANUAL = "manual"
    MONITORED = "monitored"
    REMOVED = "removed"
    UNDECIDED = "undecided"
    VANISHED = "vanished"

    def __str__(self) -> str:
        return str(self.value)
