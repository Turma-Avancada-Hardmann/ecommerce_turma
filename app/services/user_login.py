from sqlalchemy.orm import Session
from app.db.models import Usuario
from app.contracts.imports import *
from fastapi.exceptions import HTTPException
from fastapi import status, Response


class UserLogin:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def login_user(self, login: UserLogin):
        user = (self.db_session
            .query(Usuario)
            .filter(Usuario.email == login.email).first()
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Unauthorized'
            )

        return user
