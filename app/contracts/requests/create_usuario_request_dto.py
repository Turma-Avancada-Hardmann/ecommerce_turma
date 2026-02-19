from app.contracts.base import CustomBaseModel


class CreateUserRequestDto(CustomBaseModel):
    name: str
    email: str
    password: str