from pydantic import BaseModel, EmailStr


class WaitlistCreate(BaseModel):

    name: str

    email: EmailStr


class WaitlistResponse(BaseModel):

    id: int

    name: str

    email: EmailStr

    class Config:
        from_attributes = True