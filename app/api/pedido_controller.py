from fastapi import APIRouter, Response, status, Depends
from app.services.pedido_service import PedidoService
from app.contracts.requests.create_pedido_request_dto import CreatePedidoRequestDto
from app.api.deps import get_db_session
from sqlalchemy.orm import Session


router = APIRouter(prefix='/pedido')


@router.post(
    '/insert-pedido',
)
def create_pedido(
    pedido: CreatePedidoRequestDto,
    db_session: Session = Depends(get_db_session)
):
    pedido_service = PedidoService(db_session=db_session)
    pedido_service.create_pedido(pedido)
    return Response(status_code=status.HTTP_201_CREATED)
