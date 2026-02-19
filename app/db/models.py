from app.db.base import Base
from datetime import datetime
from typing import List

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    ForeignKey,
    DECIMAL,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(155))
    email: Mapped[str] = mapped_column(String(155))
    password: Mapped[str] = mapped_column(String(155))

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    pedidos: Mapped[List["Pedido"]] = relationship(
        back_populates="usuario",
        cascade="all, delete"
    )


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    atributos: Mapped[List["AtributoProduto"]] = relationship(
        back_populates="produto",
        cascade="all, delete"
    )


class AtributoProduto(Base):
    __tablename__ = "atributos_produto"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    produto_id: Mapped[int] = mapped_column(
        ForeignKey("produtos.id", ondelete="CASCADE"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    produto: Mapped["Produto"] = relationship(
        back_populates="atributos"
    )


class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        nullable=False
    )

    total_amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="PENDING")

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    usuario: Mapped["Usuario"] = relationship(
        back_populates="pedidos"
    )