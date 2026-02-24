from sqlalchemy.orm import Session
from app.db.models import Usuario
from app.contracts.imports import *
from fastapi.exceptions import HTTPException
from fastapi import status


class ServiceUser:
    def __init__(self, db_session: Session):
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
            self.db_session.refresh(user_on_db)
            return user_on_db
        except Exception as e:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail={e}
            )
        
    def get_user_by_id(self, user_id: int):
        user = (
            self.db_session
            .query(Usuario)
            .filter(Usuario.id == user_id)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado"
            )

        return user
