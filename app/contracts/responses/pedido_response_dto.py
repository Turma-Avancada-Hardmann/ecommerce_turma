from app.contracts.base import CustomBaseModel
from app.contracts.enums.status import PedidoStatus


class PedidoResponseDto(CustomBaseModel):
    id: int
    total_amount: float
    status: PedidoStatus
    created_at: str
