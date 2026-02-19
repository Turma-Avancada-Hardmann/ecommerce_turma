from app.contracts.base import CustomBaseModel


class GetUserRequestDto(CustomBaseModel):
    id: int
