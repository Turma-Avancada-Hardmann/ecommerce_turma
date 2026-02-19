from app.contracts.base import CustomBaseModel


class UserResponseDto(CustomBaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: str