from enum import Enum


class SoundsValue(str, Enum):
    ALIEN = "alien"
    BIKE = "bike"
    BUGLE = "bugle"
    CASHREGISTER = "cashregister"
    CLASSICAL = "classical"
    CLIMB = "climb"
    COSMIC = "cosmic"
    DISABLED = "disabled"
    ECHO = "echo"
    FALLING = "falling"
    GAMELAN = "gamelan"
    INCOMING = "incoming"
    INTERMISSION = "intermission"
    MAGIC = "magic"
    MECHANICAL = "mechanical"
    NONE = "none"
    PERSISTENT = "persistent"
    PIANOBAR = "pianobar"
    PUSHOVER = "pushover"
    SIREN = "siren"
    SPACEALARM = "spacealarm"
    TUGBOAT = "tugboat"
    UPDOWN = "updown"
    VIBRATE = "vibrate"

    def __str__(self) -> str:
        return str(self.value)
