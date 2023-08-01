from pydantic import BaseModel, EmailStr


# Pydantic model for creating a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    username: str
    admin: bool
    subscriber: bool
    hashed_password: str


# Pydantic model for reading a user
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    username: str
    admin: bool
    subscriber: bool


# Pydantic model for the hashed password
class UserInDB(BaseModel):
    hashed_password: str
