from fastapi import APIRouter, Header, HTTPException, status

from app.config.i18n import get_locale, t
from app.schemas.contact import ContactForm
from app.services.email_service import send_contact_email

router = APIRouter()


@router.post("/contact", status_code=status.HTTP_200_OK)
async def contact(
    form: ContactForm,
    accept_language: str | None = Header(default=None),
):
    locale = get_locale(accept_language)
    try:
        await send_contact_email(
            last_name=form.last_name,
            first_name=form.first_name,
            email=form.email,
            company=form.company,
            message=form.message,
        )
        return {"message": t("contact.success", locale)}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=t("contact.error", locale),
        )