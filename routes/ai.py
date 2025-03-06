from fastapi import APIRouter, Depends
from auth import verify_token

router = APIRouter()

@router.get("/ai/predict")
async def ai_predict(user=Depends(verify_token)):
    return {"message": f"AI processing for {user}"}
