from fastapi import APIRouter, Depends, HTTPException
from database import db
from models import UserSchema
from auth import AuthJWT
from bson import ObjectId
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup")
async def signup(user: UserSchema):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user.password = pwd_context.hash(user.password)
    new_user = await db.users.insert_one(user.dict())
    return {"message": "User created", "id": str(new_user.inserted_id)}

@router.post("/login")
async def login(user: UserSchema, Authorize: AuthJWT = Depends()):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    access_token = Authorize.create_access_token(subject=str(db_user["_id"]))
    return {"access_token": access_token}

@router.get("/protected")
async def protected(user_id: str = Depends(AuthJWT().get_jwt_subject)):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    return {"message": "Welcome!", "user": user["username"]}