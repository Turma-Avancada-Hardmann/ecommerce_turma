from app.contracts.base import CustomBaseModel
from pydantic import EmailStr, field_validator
import re


class UserLogin(CustomBaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(cls, password: str):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')

        if not re.search(r'\d', password):
            raise ValueError('Password must contain at least one number')

        if not re.search(r'[A-Z]', password):
            raise ValueError('Password must contain at least one uppercase letter')

        if not re.search(r'[a-z]', password):
            raise ValueError('Password must contain at least one lowercase letter')

        if not re.search(r'[@$!%*?&#]', password):
            raise ValueError('Password must contain at least one special character (@, $, !, %, *, ?, or &)')

        return password
