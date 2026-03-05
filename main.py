from fastapi import FastAPI
from app.api.user_controller import router as user_router
from app.api.product_controller import router as product_router
from app.api.pedido_controller import router as pedido_router
from app.api.user_login_controller import router as login_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(pedido_router)
app.include_router(login_router)
