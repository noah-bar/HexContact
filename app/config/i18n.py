TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        "contact.success": "Your message has been sent successfully.",
        "contact.error": "Failed to send email.",
    },
    "fr": {
        "contact.success": "Votre message a bien été envoyé.",
        "contact.error": "Erreur lors de l'envoi de l'email.",
    },
}

DEFAULT_LOCALE = "en"


def get_locale(accept_language: str | None) -> str:
    if not accept_language:
        return DEFAULT_LOCALE
    lang = accept_language.split(",")[0].split(";")[0].strip()[:2].lower()
    return lang if lang in TRANSLATIONS else DEFAULT_LOCALE


def t(key: str, locale: str) -> str:
    return TRANSLATIONS.get(locale, TRANSLATIONS[DEFAULT_LOCALE]).get(key, key)