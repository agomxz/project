from fastapi import APIRouter

from app.api.api_v1.endpoints.health_check import router as health_check_router
from app.api.api_v1.endpoints.transactions import router as transactions_router

api_router = APIRouter()
api_router.include_router(health_check_router, tags=["Health_Check"])
api_router.include_router(transactions_router, tags=["Transactions"])
