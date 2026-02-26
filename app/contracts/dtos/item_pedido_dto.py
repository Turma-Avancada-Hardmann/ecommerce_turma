from app.contracts.base import CustomBaseModel


class ItemPedidoDto(CustomBaseModel):
    produto_id: int
    quantidade: int
