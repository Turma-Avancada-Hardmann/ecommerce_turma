from app.contracts.base import CustomBaseModel
from app.contracts.dtos.item_pedido_dto import ItemPedidoDto
from typing import List


class CreatePedidoRequestDto(CustomBaseModel):
    usuario_id: int
    itens: List[ItemPedidoDto]
