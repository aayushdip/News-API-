from pydantic import BaseModel, EmailStr
from datetime import date


class Company(BaseModel):
    name: str
    founded_date: date
    country: str
    website: str
    email: EmailStr
    contact_no: str
