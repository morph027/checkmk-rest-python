from enum import Enum


class GetMetricReduce(str, Enum):
    AVERAGE = "average"
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
