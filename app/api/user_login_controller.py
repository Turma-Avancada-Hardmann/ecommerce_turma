from fastapi import APIRouter, Response, status, Depends
from app.services.user_login import UserLogin
from app.contracts.requests.user_login import UserLogin as Login
from app.api.deps import get_db_session
from sqlalchemy.orm import Session


router = APIRouter()

@router.post(
    '/login',
    status_code=status.HTTP_201_CREATED
)
def logging_user(
    user: Login,
    db_session: Session = Depends(get_db_session)
):
    user_login = UserLogin(db_session=db_session)
    user_login.login_user(user)
