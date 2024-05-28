# main.py

from fastapi import FastAPI
from app.user_routes import router as user_router
from app.customer_routes import router as customer_router
from app.database import create_pool, close_pool
from app.manufacturing_routes import router as manufacturing_router
from app.suppliers import router as supplier_router

app = FastAPI()

# Include the user router
app.include_router(user_router, prefix="/users")

# Include the customer router
app.include_router(customer_router, prefix="/customers")

# Include the manufacture router
app.include_router(manufacturing_router, prefix="/manufacture")

# Include the suppliers router
app.include_router(supplier_router, prefix="/supplier")

# Create the database connection pool
@app.on_event("startup")
async def startup():
    await create_pool()

# Close the database connection pool
@app.on_event("shutdown")
async def shutdown():
    await close_pool()