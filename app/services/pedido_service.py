from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models import Pedido, ItemPedido, Produto
from app.contracts.requests.create_pedido_request_dto import CreatePedidoRequestDto
from fastapi import HTTPException, status


class PedidoService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_pedido(self, create_request_dto: CreatePedidoRequestDto) -> Pedido:

        pedido = Pedido(
            usuario_id=create_request_dto.usuario_id,
            total_amount=0,
            status="PENDING"
        )

        self.db_session.add(pedido)
        self.db_session.flush()

        total = 0

        for item in create_request_dto.itens:

            produto = self.db_session.execute(
                select(Produto).where(Produto.id == item.produto_id)
            ).scalar_one_or_none()

            if not produto:
                raise HTTPException(
                    detail=f"Produto {item.produto_id} não encontrado",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            if not produto.active:
                raise HTTPException(
                    detail=f"Produto {produto.id} está inativo",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            preco_unitario = float(produto.price)
            subtotal = preco_unitario * item.quantidade

            total += subtotal

            item_pedido = ItemPedido(
                pedido_id=pedido.id,
                produto_id=produto.id,
                quantidade=item.quantidade,
                preco_unitario=preco_unitario,
                subtotal=subtotal
            )

            self.db_session.add(item_pedido)

        pedido.total_amount = total

        self.db_session.commit()
        self.db_session.refresh(pedido)

        return pedido