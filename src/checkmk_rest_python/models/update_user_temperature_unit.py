from enum import Enum


class UpdateUserTemperatureUnit(str, Enum):
    CELSIUS = "celsius"
    DEFAULT = "default"
    FAHRENHEIT = "fahrenheit"

    def __str__(self) -> str:
        return str(self.value)
