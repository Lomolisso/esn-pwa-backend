from sqlalchemy.orm import Session
from app.api.model import models
from app.api.model import schemas
from sqlalchemy import select, update

# --- Crud utils for ConnectionRequest ---

def get_conn_requests(session: Session, page=0, page_size=10) -> list[models.ConnectionRequest]:
    query = select(models.ConnectionRequest).offset(page).limit(page_size)
    result = session.execute(query)
    return result.scalars().all()

def get_conn_request_by_uuid(session: Session, uuid: str) -> models.ConnectionRequest:
    query = select(models.ConnectionRequest).where(
        models.ConnectionRequest.uuid == uuid
    )
    result = session.execute(query)
    return result.scalars().all()

def create_conn_request(session: Session, conn_request: schemas.ConnectionRequestIn) -> models.ConnectionRequest:
    db_instance = models.ConnectionRequest(**conn_request.dict())
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return db_instance

def update_conn_request(session: Session, uuid: str, fields: dict) -> models.ConnectionRequest:
    query = update(models.ConnectionRequest).where(
        models.ConnectionRequest.uuid == uuid
    ).values(fields)
    session.execute(query)
    session.commit()
    return get_conn_request_by_uuid(session=session, uuid=uuid)

# --- Crud utils for EdgeGateway ---

def get_edge_gateways(session: Session, page=0, page_size=10) -> list[models.EdgeGateway]:
    query = select(models.EdgeGateway).offset(page).limit(page_size)
    result = session.execute(query)
    return result.scalars().all()

def get_edge_gateway_by_uuid(session: Session, uuid) -> models.EdgeGateway:
    query = select(models.EdgeGateway).where(
        models.EdgeGatway.uuid == uuid
    )
    result = session.execute(query)
    return result.scalars().first()

def create_edge_gateway(session: Session, edge_gateway: schemas.EdgeGatewayIn) -> models.EdgeGateway:
    db_instance = models.EdgeGateway(**edge_gateway.dict())
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return db_instance

def update_edge_gateway(session: Session, uuid: str, fields: dict) -> models.EdgeGateway:
    query = update(models.EdgeGateway).where(
        models.EdgeGateway.uuid == uuid
    ).values(fields)
    session.execute(query)
    session.commit()
    return get_edge_gateway_by_uuid(session=session, uuid=uuid)

# --- Crud utils for DatasetFile ---

def get_datasets(session: Session, page=0, page_size=10) -> list[models.DatasetFile]:
    query = select(models.DatasetFile).offset(page).limit(page_size)
    result = session.execute(query)
    return result.scalars().all()

def get_dataset_file_by_uuid(session: Session, uuid) -> models.DatasetFile:
    query = select(models.EdgeGateway).where(models.EdgeGatway.uuid == uuid)
    result = session.execute(query)
    return result.scalars().first()

def create_dataset_file(session: Session, dataset_file: schemas.DatasetFileIn) -> models.DatasetFile:
    db_instance = models.DatasetFile(**dataset_file.dict())
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return db_instance

def update_dataset_file(session: Session, uuid: str, fields: dict) -> models.DatasetFile:
    query = update(models.DatasetFile).where(
        models.DatasetFile.uuid == uuid
    ).values(fields)
    session.execute(query)
    session.commit()
    return get_edge_gateway_by_uuid(session=session, uuid=uuid)