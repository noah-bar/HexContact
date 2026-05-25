from fastapi import FastAPI

from app.api.v1.router import router

app = FastAPI(title="Hex Contact API")

app.include_router(router)