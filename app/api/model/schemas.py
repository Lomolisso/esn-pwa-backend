from datetime import datetime
from pydantic import BaseModel, Field
from app.api.model import enums

# ------------------ model-related schemas ------------------

        
class BaseDatasetFile(BaseModel):
    """
    Basic dataset schema.
    """

    dataset_name = Field(max_length=100)
    filetype : enums.SupportedFileType


class DatasetFileIn(BaseDatasetFile):
    """
    Schema for creating a dataset instance.
    """
    pass

class DatasetFileOut(BaseDatasetFile):
    """
    Schema for reading/returning a dataset data.
    """

    uuid : str = Field(max_length=50)
    dataset_name : str 
    filetype : str 

    class Config:
        orm_mode = True


class BaseEdgeGateway(BaseModel):
    """
    Basic register gateway request.
    """

    device_name : str = Field(max_length=50)
    mac_address : str = Field(max_length=17)
    ip_address : str = Field(max_length=15)

class EdgeGatewayIn(BaseEdgeGateway):
    """
    Schema for creating an edge gateway.
    """
    pass

class EdgeGatewayOut(BaseEdgeGateway):
    uuid : str = Field(max_length=50)
    device_status : enums.EdgeGatewayStatus
    predictive_model_type : enums.PredictiveModel | None
    dataset : DatasetFileOut | None
    
    class Config:
        orm_mode = True


class ConnectionRequestIn(BaseEdgeGateway):
    """
    Schema for creating a conn gateway request.
    """
    pass


class ConnectionRequestOut(BaseEdgeGateway):
    """
    Schema for reading/returning register gateway requests.
    """

    uuid : str = Field(max_length=50)
    request_status : enums.ConnectionRequestStatus
    recieved_at : datetime
    reviewed_at : datetime

    class Config:
        orm_mode = True


        
# --- Interaction-related schemes ---

class BluetoothDevice(BaseModel):
    device_name : str = Field(max_length=50)
    mac_address : str = Field(max_length=17)
    status : str

class BluetoothScannedDevices(BaseModel):
    devices : list[BluetoothDevice]