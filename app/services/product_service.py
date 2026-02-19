from sqlalchemy.orm import Session
from app.db.models import Produto
from app.contracts.imports import *
from fastapi.exceptions import HTTPException
from fastapi import status


class ProductService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_product(self, product: CreateProductRequestDto):
        product_on_db = Produto(
            name=product.name,
            description=product.description,
            price=product.price,
            active=product.active
        )

        try:
            self.db_session.add(product_on_db)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={e}
            )
