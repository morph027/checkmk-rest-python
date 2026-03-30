from enum import Enum


class DiscoverServicesMode(str, Enum):
    FIX_ALL = "fix_all"
    NEW = "new"
    ONLY_HOST_LABELS = "only_host_labels"
    ONLY_SERVICE_LABELS = "only_service_labels"
    REFRESH = "refresh"
    REMOVE = "remove"
    TABULA_RASA = "tabula_rasa"

    def __str__(self) -> str:
        return str(self.value)
