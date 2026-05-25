# hex-contact

Minimal FastAPI service that handles a contact form and sends an email via SMTP.

## Features

- `POST /api/v1/contact` — validates the form and sends an email
- `GET /health` — health check endpoint
- Rate limiting: 5 requests per hour per IP
- i18n: response messages in English and French (`Accept-Language` header)
- Honeypot field to silently reject bot submissions
- API docs disabled in production

## Environment variables

Copy `.env.example` to `.env` and fill in the values.

| Variable | Required | Default | Description |
|---|---|---|---|
| `ENVIRONMENT` | No | `development` | Set to `production` to disable `/docs` |
| `SMTP_HOST` | Yes | — | SMTP server hostname |
| `SMTP_PORT` | No | `587` | SMTP server port |
| `SMTP_USERNAME` | Yes | — | SMTP login username |
| `SMTP_PASSWORD` | Yes | — | SMTP login password |
| `MAIL_TO_CONTACT` | Yes | — | Recipient email address |
| `CORS_ORIGINS` | No | `["*"]` | Allowed origins (JSON array) |

## Run locally

```bash
uv sync
uv run fastapi dev app/main.py
```

## Deploy with Docker

```bash
cp .env.example .env
# fill in .env values
chmod 600 .env

docker compose up -d --build
```

The API will be available at `http://localhost:8000`.  
Put Nginx or Caddy in front to handle TLS.

## API

### POST /api/v1/contact

**Request body** (camelCase or snake_case accepted):

```json
{
  "firstName": "Jean",
  "lastName": "Dupont",
  "email": "jean@example.com",
  "company": "Acme",
  "message": "Hello!"
}
```

> Add a hidden `website` field in your form and leave it empty — it acts as a honeypot to silently reject bot submissions.

**Responses:**

| Status | Description |
|---|---|
| `200` | Email sent successfully |
| `422` | Validation error |
| `429` | Rate limit exceeded |
| `500` | Failed to send email |

### GET /health

```json
{ "status": "ok" }
```