from app.database import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.types import Integer, String, PickleType, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.api.model import enums


import os
import uuid
import app.utils as utils

class ConnectionRequest(Base):
    __tablename__ = "connection_request_table"
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # admin_id = Column(Integer, ForeignKey("user.id")
    
    device_name = Column(String(50), nullable=False)
    mac_address = Column(String(17), nullable=False)
    ip_address = Column(String(15), nullable=False)

    conn_status = Column(Enum(enums.ConnectionRequestStatus), default=enums.ConnectionRequestStatus.NOT_SET)
    recieved_at = Column(DateTime, default=utils.tz_now)
    reviewed_at = Column(DateTime, nullable=True)

    
class EdgeGateway(Base):
    __tablename__ = "edge_gateway_table"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # admin_id = Column(Integer, ForeignKey("user.id"))
    
    device_name = Column(String(50), nullable=False, unique=True)
    mac_address = Column(String(17), nullable=False, unique=True)
    ip_address = Column(String(15), nullable=False, unique=True)
    
    device_status = Column(Enum(enums.EdgeGatewayStatus), default=enums.EdgeGatewayStatus.WAITING_CONFIG)
    predictive_model_type = Column(Enum(enums.PredictiveModel), nullable=True)
    predictive_model = Column(PickleType, nullable=True) 

    dataset = Column(Integer, ForeignKey("dataset_file_table.id"))

class DatasetFile(Base):
    _PATH = "/app/train_data"

    __tablename__ = "dataset_file_table"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # admin_id = Column(Integer, ForeignKey("user.id"))

    dataset_name = Column(String(100), nullable=False, unique=True)
    filetype = Column(Enum(enums.SupportedFileType), nullable=False)

    def get_filepath(self):
        return os.path.join(f"{self.uuid}.{self.filetype}")

