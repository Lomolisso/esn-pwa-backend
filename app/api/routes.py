"""
Routes for the api.

13/11/2022
"""


from fastapi import APIRouter, Depends
from app.dependencies import get_session
from app.api.model import schemas, crud, enums
from app.api import utils as api_utils
from sqlalchemy.orm import Session


PAGE_SIZE = 8


api_router = APIRouter(prefix="/api")

# --- Origin: Edge gateway ---        

@api_router.post("/conn-request", status_code=200)
async def submit_conn_request(conn_request: schemas.ConnectionRequestIn, session: Session = Depends(get_session)):
    conn_request = crud.create_conn_request(
        session=session,
        conn_request=conn_request
    )
        

# --- Origin: Frontend ---
    
@api_router.post("/accept-conn-request/{request_uuid}", status_code=200, response_model=schemas.EdgeGatewayOut)
async def accept_conn_request(request_uuid: str, session = Depends(get_session)):
    """
    Accepts an incoming connection request from an edge gateway.
    """

    conn_request = api_utils.process_conn_request(
        session=session,
        request_uuid=request_uuid,
        status=enums.ConnectionRequestStatus.CONN_ACCEPTED
    )

    return conn_request

@api_router.post("/deny-conn-request/{request_uuid}", status_code=200, response_model=schemas.EdgeGatewayOut)
async def deny_conn_request(request_uuid: str, session = Depends(get_session)):
    """
    Denies an incoming connection request from an edge gateway.
    """

    conn_request = api_utils.process_conn_request(
        session=session,
        request_uuid=request_uuid,
        status=enums.ConnectionRequestStatus.CONN_DENIED
    )

    return conn_request


@api_router.get("/get-conn-requests", status_code=200, response_model=list[schemas.ConnectionRequestOut])
async def get_conn_requests(session = Depends(get_session)):
    """
    Returns a list of JSON's with the last PAGE_SIZE conn. requests
    """
    
    conn_requests = crud.get_conn_requests(
        session=session,
        page_size=PAGE_SIZE
    )
    
    return conn_requests

@api_router.get("/get-edge-gateways", status_code=200, response_model=list[schemas.EdgeGatewayOut])
async def get_edge_gateways(session = Depends(get_session)):
    """
    Returns a list of JSON's with the last PAGE_SIZE edge gateways.
    """
    
    edge_gateways = crud.get_edge_gateways(
        session=session,
        page_size=PAGE_SIZE
    )
    
    return edge_gateways

@api_router.get("/get-edge-gateway/{gateway_uuid}", status_code=200, response_model=schemas.EdgeGatewayOut)
async def get_edge_gateway(gateway_uuid: str, session = Depends(get_session)):
    """
    Returns an edge gateway.
    """
    
    edge_gateway = crud.get_edge_gateway_by_uuid(
        session=session,
        uuid=gateway_uuid
    )
    
    return edge_gateway

@api_router.get("/get-datasets", status_code=200, response_model=list[schemas.DatasetFileOut])
async def get_dataset(session = Depends(get_session)):
    """
    Returns a list of JSON's with the last PAGE_SIZE datasets.
    """
    
    datasets = crud.get_datasets(
        session=session,
        page_size=PAGE_SIZE
    )
    
    return datasets

@api_router.get("/get-dataset/{dataset_uuid}", status_code=200, response_model=schemas.DatasetFileOut)
async def get_dataset(dataset_uuid: str, session = Depends(get_session)):
    """
    Returns a dataset_file.
    """
    
    dataset = crud.get_dataset_file_by_uuid(
        session=session,
        uuid=dataset_uuid
    )
    
    return dataset

