from app.contracts.base import CustomBaseModel


class ProductResponseDto(CustomBaseModel):
    name: str
    description: str
    price: float
    active: bool
