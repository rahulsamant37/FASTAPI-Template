from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str

class UserV1(UserBase):
    id: int

class UserV2(UserV1):
    email: EmailStr

class UserInDB(UserV2):
    # Additional fields that might be in the database but not in API responses
    password_hash: str