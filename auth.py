from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from fastapi_jwt_auth.exceptions import AuthJWTException

"""
Depends:           Used for dependency injection (we use it later for verifying JWT tokens).
HTTPException:     To return errors when authentication fails.
AuthJWT:           The main JWT authentication handler.
BaseModel, Field:  Pydantic's way of handling data validation.
os: Used to read   environment variables (like secret keys).
load_dotenv:       Loads values from a .env file into the environment.
AuthJWTException:  Catches JWT authentication-related errors.

"""

load_dotenv() #Loads all key-value pairs from a .env file into the environment.

class Settings(BaseModel):
    authjwt_secret_key: str = Field(..., alias="JWT_SECRET")

    class Config:
        env_file = ".env" # It tells Pydantic to load values from .env.
        allow_population_by_field_name = True #Allows using the field name (authjwt_secret_key) instead of the alias (JWT_SECRET).

@AuthJWT.load_config #A decorator that automatically loads JWT settings.
def get_config():
    return Settings(authjwt_secret_key=os.getenv("JWT_SECRET"))

def verify_token(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        return Authorize.get_jwt_subject()
    except AuthJWTException:
        raise HTTPException(status_code=401, detail="Invalid or Expired Token")