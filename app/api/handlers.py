from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

from app.config.i18n import get_locale, t_validation


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    locale = get_locale(request.headers.get("accept-language"))

    errors = [
        {
            "field": err["loc"][-1],
            "message": t_validation(err["type"], locale),
        }
        for err in exc.errors()
    ]

    return JSONResponse(status_code=422, content={"errors": errors})


async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit exceeded: {exc.detail}"},
    )