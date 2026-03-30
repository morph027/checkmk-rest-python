from enum import Enum


class ActivationSiteStatusPhase(str, Enum):
    ACTIVATE = "activate"
    DONE = "done"
    FINISHING = "finishing"
    INITIALIZED = "initialized"
    QUEUED = "queued"
    STARTED = "started"
    SYNC = "sync"

    def __str__(self) -> str:
        return str(self.value)
