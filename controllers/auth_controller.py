from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.request.auth_request import LoginRequest
from services.auth_service import AuthService

from configs.database import get_db
from utils.response import response_success

auth_router = APIRouter()


@auth_router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return response_success(AuthService(db).login(request))
