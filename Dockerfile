# ── Build stage ───────────────────────────────────────────────────────────────
FROM python:3.14-slim AS builder

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.10.7 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app/ ./app/
RUN uv sync --frozen --no-dev


# ── Runtime stage ─────────────────────────────────────────────────────────────
FROM python:3.14-slim

WORKDIR /app

RUN adduser --disabled-password --no-create-home appuser

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/app ./app/

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]