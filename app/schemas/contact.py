from pydantic import BaseModel, EmailStr


class ContactForm(BaseModel):
    last_name: str
    first_name: str
    email: EmailStr
    company: str | None = None
    message: str | None = None