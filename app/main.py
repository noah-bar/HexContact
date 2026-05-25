import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.api.handlers import rate_limit_exceeded_handler, validation_exception_handler
from app.api.v1.router import router
from app.config.env import env
from app.config.limiter import limiter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

_is_production = env.environment == "production"

app = FastAPI(
    title="Hex Contact API",
    docs_url=None if _is_production else "/docs",
    redoc_url=None if _is_production else "/redoc",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=env.cors_origins,
    allow_methods=["POST"],
    allow_headers=["Content-Type", "Accept-Language"],
)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Routers
app.include_router(router)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

# Exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)