from fastapi import APIRouter, Response, status, Depends
from app.services.user_service import ServiceUser
from app.contracts.imports import UserResponseDto
from app.contracts.imports import CreateUserRequestDto
from app.contracts.imports import GetUserRequestDto
from app.api.deps import get_db_session
from sqlalchemy.orm import Session


router = APIRouter(prefix='/user')


@router.post(
    '/create-user',
    response_model=UserResponseDto,
    status_code=status.HTTP_201_CREATED
)
def create_user_controller(
    user: CreateUserRequestDto,
    db_session: Session = Depends(get_db_session)
):
    service_user = ServiceUser(db_session)
    created = service_user.create_user(user=user)
    return UserResponseDto(
        id=created.id,
        name=created.name,
        email=created.email,
        password=created.password,
        created_at=created.created_at.isoformat() if created.created_at else None
    )

@router.get(
    '/get-user-by-id/{user_id}',
    response_model=UserResponseDto,
    status_code=status.HTTP_200_OK
)
def get_user_by_id_controller(
    user_id: int,
    db_session: Session = Depends(get_db_session)
) -> UserResponseDto:
    user_service = ServiceUser(db_session=db_session)
    user = user_service.get_user_by_id(user_id=user_id)
    return UserResponseDto(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password,
        created_at=user.created_at.isoformat() if user.created_at else None
    )
