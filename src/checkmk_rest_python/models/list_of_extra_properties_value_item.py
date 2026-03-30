from enum import Enum


class ListOfExtraPropertiesValueItem(str, Enum):
    ABSTIME = "abstime"
    ACK_AUTHOR = "ack_author"
    ACK_COMMENT = "ack_comment"
    ADDRESS = "address"
    CONTEXT = "context"
    HOSTTAGS = "hosttags"
    LONGOUTPUT = "longoutput"
    NOTESURL = "notesurl"
    NOTIFICATION_AUTHOR = "notification_author"
    NOTIFICATION_COMMENT = "notification_comment"
    OMD_SITE = "omd_site"
    PERFDATA = "perfdata"
    RELTIME = "reltime"

    def __str__(self) -> str:
        return str(self.value)
