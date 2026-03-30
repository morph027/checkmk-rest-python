from enum import Enum


class CmkGuiOpenapiEndpointsAgentDownloadAgentOsType(str, Enum):
    LINUX_DEB = "linux_deb"
    LINUX_RPM = "linux_rpm"
    WINDOWS_MSI = "windows_msi"

    def __str__(self) -> str:
        return str(self.value)
