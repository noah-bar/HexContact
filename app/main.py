from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.handlers import validation_exception_handler
from app.api.v1.router import router

app = FastAPI(title="Hex Contact API")

app.include_router(router)
app.add_exception_handler(RequestValidationError, validation_exception_handler)