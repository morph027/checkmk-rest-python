from enum import Enum


class GetMetricType(str, Enum):
    PREDEFINED_GRAPH = "predefined_graph"
    SINGLE_METRIC = "single_metric"

    def __str__(self) -> str:
        return str(self.value)
