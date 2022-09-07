from fastapi import FastAPI
from pydantic import BaseModel

class customer(BaseModel):
    first_name:str
    last_name:str
    mobile_no:str
    email:str
    company_name:str
    city:str

class orm():
    orm_mode=True