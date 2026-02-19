from sqlalchemy.orm import Session
from app.db.models import Usuario
from app.contracts.imports import *
from fastapi.exceptions import HTTPException
from fastapi import status


class ServiceUser:
    def __int__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, user: CreateUserRequestDto):
        user_on_db = Usuario(
            name=user.name,
            email=user.email,
            password=user.password
        )

        self.db_session.add(user_on_db)

        try:
            self.db_session.commit()
        except Exception as e:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail={e}
            )
        
    def get_user_by_id(self, user_id: GetUserRequestDto):
        return (
            self.db_session.query(Usuario).
            filter(Usuario.id == user_id.id)
        )
