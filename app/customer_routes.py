# app/customer_routes.py

from fastapi import APIRouter, HTTPException
from app.models import Customer
from app.database import execute_query, fetch_one, fetch_all

router = APIRouter()

@router.post("/create")
async def create_customer(customer: Customer):
    query = """
        INSERT INTO customers (customer_name, customer_email, customer_phone,customer_address )
        VALUES ($1, $2, $3, $4)
    """
    try:
        await execute_query(query, customer.customer_name, customer.customer_email, customer.customer_phone, customer.customer_address)
        return {"message": "Customer created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.put("/update/{customer_id}")
async def update_customer(customer_id: int, customer: Customer):
    query = """
        UPDATE customers
        SET customer_name = $1, customer_email = $2, customer_phone = $3,customer_address = $4
        WHERE id = $5
    """
    try:
        await execute_query(query, customer.customer_name, customer.customer_email, customer.customer_phone,customer.customer_address, customer_id)
        return {"message": "Customer updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.delete("/delete/{customer_id}")
async def delete_customer(customer_id: int):
    query = """
        DELETE FROM customers
        WHERE id = $1
    """
    try:
        await execute_query(query, customer_id)
        return {"message": "Customer deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/read_all")
async def read_all_customers():
    query = """
        SELECT * FROM customers
    """
    try:
        customers = await fetch_all(query)
        return customers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")