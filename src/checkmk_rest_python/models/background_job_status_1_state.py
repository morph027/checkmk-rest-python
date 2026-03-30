from enum import Enum


class BackgroundJobStatus1State(str, Enum):
    EXCEPTION = "exception"
    FINISHED = "finished"
    INITIALIZED = "initialized"
    RUNNING = "running"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
