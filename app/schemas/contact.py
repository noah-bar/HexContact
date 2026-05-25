from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class ContactForm(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    last_name: str
    first_name: str
    email: EmailStr
    company: str | None = None
    message: str | None = None