from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    password: str


class Customer(BaseModel):
    customer_name: str
    customer_email: EmailStr
    customer_phone: str
    customer_address : str