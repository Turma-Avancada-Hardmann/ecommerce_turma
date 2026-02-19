from app.contracts.base import CustomBaseModel


class CreateProductRequestDto(CustomBaseModel):
    name: str
    description: str
    price: float
    active: bool