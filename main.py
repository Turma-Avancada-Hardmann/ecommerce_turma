from fastapi import FastAPI
from app.api.user_controller import router as user_router
from app.api.product_controller import router as product_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
