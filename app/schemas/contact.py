from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel


class ContactForm(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    last_name: str = Field(min_length=1, max_length=100)
    first_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    company: str | None = Field(default=None, max_length=150)
    message: str | None = Field(default=None, max_length=2000)
    # Honeypot — must remain empty; bots fill it automatically
    website: str | None = Field(default=None, exclude=True)