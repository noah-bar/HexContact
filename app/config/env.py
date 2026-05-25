from pydantic_settings import BaseSettings


class Env(BaseSettings):
    smtp_host: str
    smtp_port: int = 587
    smtp_username: str
    smtp_password: str
    mail_to_contact: str

    model_config = {"env_file": ".env"}


env = Env()