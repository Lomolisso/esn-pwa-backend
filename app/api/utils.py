from app.api.model import crud, schemas
from app.utils import tz_now

async def process_conn_request(session, request_uuid, status):
    update_fields = {
        "conn_status": status,
        "reviewed_at": tz_now()
    }
    conn_request = crud.update_conn_request(
        session=session,
        uuid=request_uuid,
        fields=update_fields
    )

    edge_gateway = crud.create_edge_gateway(
        session=session,
        edge_gateway=schemas.EdgeGatewayIn(
            device_name=conn_request.device_name,
            mac_address=conn_request.mac_address,
            ip_address=conn_request.ip_address
        )
    )
    return edge_gateway
