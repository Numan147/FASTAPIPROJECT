from enum import unique
from multiprocessing.spawn import import_main_path
from sqlalchemy import Column, Integer, String
from database import Base

class Cdetails(Base):
    __tablename__ = 'details'

    id=Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    mobile_no=Column(Integer, unique=True)
    email=Column(String)
    company_name=Column(String)
    city=Column(String)
