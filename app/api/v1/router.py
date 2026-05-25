from fastapi import APIRouter

from app.api.v1.endpoints import contact

router = APIRouter(prefix="/api/v1")
router.include_router(contact.router, tags=["contact"])