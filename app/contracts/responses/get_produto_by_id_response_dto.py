from app.contracts.base import CustomBaseModel


class GetProductByIdDto(CustomBaseModel):
    id: int
