import enum

class PredictiveModel(str, enum.Enum):
    ...

class SupportedFileType(str, enum.Enum):
    ...

class ConnectionRequestStatus(str, enum.Enum):
    NOT_SET = "NOT_SET"
    CONN_ACCEPTED = "CONN_ACCEPTED"
    CONN_DENIED =  "CONN_DENIED"

class EdgeGatewayStatus(str, enum.Enum):
    WAITING_CONFIG = "WAITING_CONFIG"
    READY_TO_CONNECT = "READY_TO_CONNECT"
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"