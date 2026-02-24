from fastapi import APIRouter, Response, status, Depends
from app.services.product_service import ProductService
from app.contracts.imports import (
    ProductResponseDto,
    CreateProductRequestDto
)
from app.api.deps import get_db_session
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix='/products')


@router.post(
    '/create-product',
    response_model=ProductResponseDto,
    status_code=status.HTTP_201_CREATED
)
def create_product_controller(
    product: CreateProductRequestDto,
    db_session: Session = Depends(get_db_session)
) -> ProductResponseDto:
    product_service = ProductService(db_session=db_session)
    product_service.create_product(product)

    return ProductResponseDto(
        name=product.name,
        description=product.description,
        price=product.price,
        active=product.active
    )

@router.get(
    '/get-all-products',
)
def get_products(
    db_session: Session = Depends(get_db_session)
) -> List[ProductResponseDto]:
    product_service = ProductService(db_session=db_session)

    products = product_service.get_all_products()

    return products
