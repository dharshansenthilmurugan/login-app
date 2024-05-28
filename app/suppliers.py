from fastapi import APIRouter, HTTPException, Body
from app.models import Suppliers,SupplierProduct, Order, DeliverySchedule
from app.database import execute_query, fetch_one, fetch_all
from typing import List
from pydantic import BaseModel
import asyncpg


router = APIRouter()

@router.post("/suppliers/create")
async def create_suppliers(suppliers: Suppliers):
    print("inside function")
    query = """
        INSERT INTO suppliers (supplier_id, supplier_name, supplier_email, supplier_phone, supplier_address)
        VALUES ($1, $2, $3, $4, $5)
    """
    print("query", query)
    try:
        await execute_query(query, suppliers.supplier_id, suppliers.supplier_name, suppliers.supplier_email, suppliers.supplier_phone, suppliers.supplier_address)
        return {"message": "Supplier created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")   

@router.get("/suppliers/read_all")
async def read_all_suppliers():
    print("inside function")
    query = """
        SELECT * FROM suppliers
    """
    print("query",query)
    try:
        Suppliers = await fetch_all(query)
        print("suppliers", Suppliers)
        return Suppliers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/suppliers/{supplier_id}")
async def read_one_supplier(supplier_id: int):
    query = """
        SELECT * FROM suppliers
        WHERE supplier_id = $1
    """
    result = await fetch_one(query, supplier_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="supplier not found")



@router.put("/suppliers/{supplier_id}")
async def update_supplier(supplier_id: int, supplier: Suppliers):
    query_update = """
        UPDATE suppliers
        SET
            supplier_name = $1,
            supplier_email = $2,
            supplier_phone = $3,
            supplier_address = $4
        WHERE supplier_id = $5
    """
    query_select = """
        SELECT * FROM suppliers
        WHERE supplier_id = $1
    """
    try:
        await execute_query(query_update, supplier.supplier_name, supplier.supplier_email, supplier.supplier_phone, supplier.supplier_address, supplier_id)
        updated_supplier = await fetch_one(query_select, supplier_id)
        return {"message": "Supplier updated successfully", "supplier": updated_supplier}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/suppliers/delete/{supplier_id}")
async def delete_suppliers(supplier_id: int):
    query = """
        DELETE FROM suppliers
        WHERE supplier_id = $1
    """
    try:
        await execute_query(query, supplier_id)
        return {"message": "suppliers deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    

@router.post("/suppliers_product/create")
async def create_supplier_product(supplier_product: SupplierProduct):
    print("inside function")
    
    query_check_supplier = """
        SELECT EXISTS (SELECT 1 FROM suppliers WHERE supplier_id = $1)
    """

    query_insert_product = """
        INSERT INTO supplier_products (product_id, supplier_id, product_name, product_description, price)
        VALUES ($1, $2, $3, $4, $5)
    """
    
    try:
        supplier_exists = await fetch_one(query_check_supplier, supplier_product.supplier_id)
        if not supplier_exists['exists']:
            raise HTTPException(status_code=400, detail=f"Supplier with ID {supplier_product.supplier_id} does not exist")
        
        # Insert the supplier product
        await execute_query(query_insert_product, supplier_product.product_id, supplier_product.supplier_id, supplier_product.product_name, supplier_product.product_description, supplier_product.price)
        
        return {"message": "Supplier product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")  


@router.get("/suppliers_product/read_all")
async def read_all_supplier_products():
    print("Fetching all supplier products")
    
    query_fetch_all = """
        SELECT product_id, supplier_id, product_name, product_description, price FROM supplier_products
    """

    try:
    
        supplier_products = await fetch_all(query_fetch_all)
        
        return supplier_products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/supplier_product/{product_id}")
async def read_one_supplier_product(product_id: int):
    query = """
        SELECT *
        FROM supplier_products
        WHERE product_id = $1
    """
    result = await fetch_one(query, product_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Supplier product not found")


@router.put("/supplier_product/{product_id}")
async def update_supplier_product(product_id: int, product_data: SupplierProduct):
    query_update_product = """
        UPDATE supplier_products
        SET
            product_name = $1,
            product_description = $2,
            price = $3
        WHERE product_id = $4
    """
    query_select_product = """
        SELECT * FROM supplier_products
        WHERE product_id = $1
    """
    try:
        await execute_query(
            query_update_product,
            product_data.product_name,
            product_data.product_description,
            product_data.price,
            product_id
        )
        updated_product = await fetch_one(query_select_product, product_id)
        return {"message": "Supplier product updated successfully", "product": updated_product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.delete("/supplier_product/delete/{product_id}")
async def delete_supplier_product(product_id: int):
    query = """
        DELETE FROM supplier_products
        WHERE product_id = $1
    """
    try:
        await execute_query(query, product_id)
        return {"message": "Supplier product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.post("/orders/create")
async def create_order(order: Order):
    query = """
        INSERT INTO orders (order_id, supplier_id, product_id, quantity, order_date, delivery_date)
        VALUES ($1, $2, $3, $4, $5, $6)
    """
    try:
        await execute_query(
            query,
            order.order_id,
            order.supplier_id,
            order.product_id,
            order.quantity,
            order.order_date,
            order.delivery_date
        )
        return {"message": "Order created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/orders/read_all")
async def read_all_orders():
    print("inside function")
    query = """
        SELECT * FROM orders
    """
    print("query", query)
    try:
        orders = await fetch_all(query)
        print("orders", orders)
        orders_list = [Order(**order) for order in orders]
        return orders_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/orders/{order_id}")
async def read_one_order(order_id: int):
    query = """
        SELECT *
        FROM orders
        WHERE order_id = $1
    """
    result = await fetch_one(query, order_id)
    if result:
        return Order(**result)
    else:
        raise HTTPException(status_code=404, detail="Order not found")


@router.put("/order/{order_id}")
async def update_order(order_id: int, order: Order):
    query_update_order = """
        UPDATE orders
        SET
            supplier_id = $1,
            product_id = $2,
            quantity = $3,
            order_date = $4,
            delivery_date = $5
        WHERE order_id = $6
    """
    query_select_order = """
        SELECT * FROM orders
        WHERE order_id = $1
    """
    try:
        await execute_query(
            query_update_order,
            order.supplier_id,
            order.product_id,
            order.quantity,
            order.order_date,
            order.delivery_date,
            order_id
        )
        updated_order = await fetch_one(query_select_order, order_id)
        if updated_order:
            return {"message": "Order updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.delete("/orders/delete/{order_id}")
async def delete_orders(order_id: int):
    query = """
        DELETE FROM orders
        WHERE order_id = $1
    """
    try:
        await execute_query(query, order_id)
        return {"message": "Order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.post("/deliveryschedule/create")
async def create_delivery_schedule(deliveryschedule: DeliverySchedule):
    query = """
        INSERT INTO DeliverySchedule (delivery_id, order_id, supplier_id, delivery_date, status)
        VALUES ($1, $2, $3, $4, $5)
    """
    try:
        await execute_query(
            query,
            deliveryschedule.delivery_id,
            deliveryschedule.order_id,
            deliveryschedule.supplier_id,
            deliveryschedule.delivery_date,
            deliveryschedule.status
        )
        return {"message": "Delivery schedule created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/deliveryschedule/read_all")
async def read_all_delivery_schedules():
    print("inside function")
    query = """
        SELECT delivery_id, order_id, supplier_id, delivery_date, status FROM DeliverySchedule
    """
    print("query", query)
    try:
        delivery_schedules = await fetch_all(query)
        print("delivery schedules", delivery_schedules)
        return delivery_schedules
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/deliveryschedule/{delivery_id}")
async def read_one_deliveryschedule(delivery_id: int):
    query = """
        SELECT delivery_id, order_id, supplier_id, delivery_date, status FROM DeliverySchedule
        WHERE delivery_id = $1
    """
    result = await fetch_one(query, delivery_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Delivery schedule not found")


@router.put("/deliveryschedule/{delivery_id}")
async def update_deliveryschedule(delivery_id: int, delivery_schedule: DeliverySchedule):
    print("delivery schedule inside")
    query_update = """
        UPDATE DeliverySchedule
        SET order_id = $1, supplier_id = $2, delivery_date = $3, status = $4
        WHERE delivery_id = $5
    """
    query_select = """
        SELECT delivery_id, order_id, supplier_id, delivery_date, status FROM DeliverySchedule
        WHERE delivery_id = $1
    """
    print("queries", query_update, query_select)
    try:
        await execute_query(query_update, delivery_schedule.order_id, delivery_schedule.supplier_id, delivery_schedule.delivery_date, delivery_schedule.status, delivery_id)
        updated_item = await fetch_one(query_select, delivery_id)
        print("updated delivery schedule", updated_item)
        return {"message": "Delivery schedule updated successfully", "delivery_schedule": updated_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/deliveryschedule/delete/{delivery_id}")
async def delete_deliveryschedule(delivery_id: int):
    query = """
        DELETE FROM DeliverySchedule
        WHERE delivery_id = $1
    """
    try:
        await execute_query(query, delivery_id)
        return {"message": "Delivery schedule deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

class BulkDeleteRequest(BaseModel):
    supplier_ids: List[int]


@router.delete("/suppliers/bulk_delete")
async def delete_bulk_suppliers(request: BulkDeleteRequest):
    supplier_ids = request.supplier_ids
    print("Received supplier IDs:", supplier_ids)  # Add this print statement
    
    # Construct a dynamic SQL query with parameterized placeholders
    query = """
        DELETE FROM suppliers
        WHERE supplier_id = ANY($1::int[])
    """
    
    try:
        # Ensure supplier_ids is passed as a list or tuple
        await execute_query(query, [supplier_ids])
        return {"message": "Suppliers deleted successfully"}
    except asyncpg.exceptions.DataError as e:
        raise HTTPException(status_code=400, detail="Invalid data provided: " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

