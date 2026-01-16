from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from src.models.auth import Token

router = APIRouter(prefix="/auth")


@router.post("/login", description="Login Authentication", status_code=status.HTTP_200_OK, response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user_email = form_data.username
    user_password = form_data.password
    # need to authenticat users here
    # And create access tokens to return
    pass

@router.post("/register", description="Registration Authentication", status_code=status.HTTP_201_CREATED, response_model=Token)
async def register():
    pass