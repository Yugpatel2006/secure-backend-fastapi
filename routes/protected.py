from fastapi import APIRouter, Depends, Body, Security
from fastapi.security import OAuth2PasswordBearer
from auth import verify_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

@router.post("/protected/protected/protected")
async def protected_route(
    token: str = Security(oauth2_scheme),  # This ensures Swagger asks for the token
    user_data: dict = Depends(verify_token),
    custom_message: str = Body(..., embed=True)  
):
    return {
        "message": "You have access to this route!",
        "user_data": user_data,  
        "custom_message": custom_message
    }
