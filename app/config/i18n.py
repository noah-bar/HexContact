TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        "contact.success": "Your message has been sent successfully.",
        "contact.error": "Failed to send email.",
        "validation.missing": "This field is required.",
        "validation.string_type": "This field must be a string.",
        "validation.email": "Invalid email address.",
        "validation.unknown": "Invalid value.",
    },
    "fr": {
        "contact.success": "Votre message a bien été envoyé.",
        "contact.error": "Erreur lors de l'envoi de l'email.",
        "validation.missing": "Ce champ est obligatoire.",
        "validation.string_type": "Ce champ doit être une chaîne de caractères.",
        "validation.email": "Adresse email invalide.",
        "validation.unknown": "Valeur invalide.",
    },
}

DEFAULT_LOCALE = "en"

VALIDATION_ERROR_MAP: dict[str, str] = {
    "missing": "validation.missing",
    "string_type": "validation.string_type",
    "value_error": "validation.email",
}


def get_locale(accept_language: str | None) -> str:
    if not accept_language:
        return DEFAULT_LOCALE
    lang = accept_language.split(",")[0].split(";")[0].strip()[:2].lower()
    return lang if lang in TRANSLATIONS else DEFAULT_LOCALE


def t(key: str, locale: str) -> str:
    return TRANSLATIONS.get(locale, TRANSLATIONS[DEFAULT_LOCALE]).get(key, key)


def t_validation(error_type: str, locale: str) -> str:
    key = VALIDATION_ERROR_MAP.get(error_type, "validation.unknown")
    return t(key, locale)