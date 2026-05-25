from fastapi_mail import FastMail, MessageSchema, MessageType

from app.config.mailer import mail_config
from app.config.env import env


async def send_contact_email(
    last_name: str,
    first_name: str,
    email: str,
    company: str | None,
    message: str | None,
) -> None:
    body = f"""\
New contact form submission.

Last name  : {last_name}
First name : {first_name}
Email      : {email}
Company    : {company or "—"}

Message:
{message or "—"}
"""

    msg = MessageSchema(
        subject=f"[Contact] {first_name} {last_name}",
        recipients=[env.mail_to_contact],
        body=body,
        subtype=MessageType.plain,
    )

    fm = FastMail(mail_config)
    await fm.send_message(msg)