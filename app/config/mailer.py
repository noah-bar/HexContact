from fastapi_mail import ConnectionConfig

from app.config.env import env

mail_config = ConnectionConfig(
    MAIL_USERNAME=env.smtp_username,
    MAIL_PASSWORD=env.smtp_password,
    MAIL_FROM=env.smtp_username,
    MAIL_PORT=env.smtp_port,
    MAIL_SERVER=env.smtp_host,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)