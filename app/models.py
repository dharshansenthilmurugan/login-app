from datetime import datetime
from pytz import timezone, UTC
from pydantic import BaseModel, EmailStr, Field
from typing import List


class User(BaseModel):
    username: str
    password: str


class Customer(BaseModel):
    customer_name: str
    customer_email: EmailStr
    customer_phone: str
    customer_address : str

class Machines(BaseModel):
    machine_id :int
    status :str

class ProductionData(BaseModel):
    id : int
    machine_id : int
    product_id : int
    quantity  : int
    timestamp : str

class Inventory(BaseModel):
    item_id : int
    name : str
    quantity : int

class QualityReport(BaseModel):
    report_id: int
    machine_id: int
    issues_found: str
    timestamp: str

class MaintenanceSchedule(BaseModel):
    id : int
    machine_id : int
    scheduled_date : datetime
    description : str


class Suppliers(BaseModel):
    supplier_id: int
    supplier_name: str
    supplier_email: EmailStr
    supplier_phone: str = None
    supplier_address: str = None

class SupplierProduct(BaseModel):
    product_id: int
    supplier_id: int
    product_name: str
    product_description: str = None
    price: float

class Order(BaseModel):
    order_id: int
    supplier_id: int
    product_id: int
    quantity: int
    order_date: str
    delivery_date: str

class DeliverySchedule(BaseModel):
    delivery_id: int
    order_id: int
    supplier_id: int
    delivery_date: str
    status: str