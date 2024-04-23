from fastapi import FastAPI
from app.routes import router as app_router
from app.routes import customer_router

app = FastAPI()

app.include_router(app_router)
app.include_router(customer_router)
