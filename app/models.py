from pydantic import BaseModel, EmailStr , Json
from datetime import datetime
from datetime import datetime
from pytz import timezone, UTC


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
