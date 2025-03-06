from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users, ai

app = FastAPI()

# Enable CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])

@app.get("/")
def home():
    return {"message": "Welcome to the AI-Powered Coding App!"}