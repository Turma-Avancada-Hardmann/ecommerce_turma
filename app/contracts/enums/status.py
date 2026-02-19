from enum import Enum


class PedidoStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELED = "CANCELED"
    SHIPPED = "SHIPPED"
