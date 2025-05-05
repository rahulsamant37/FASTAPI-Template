from fastapi import FastAPI, APIRouter
from typing import List, Dict

# Create the main FastAPI application
app = FastAPI(title="Versioned API Example")

# Create base routers for different versions
v1_router = APIRouter(prefix="/api/v1", tags=["Users v1"])
v2_router = APIRouter(prefix="/api/v2", tags=["Users v2"])

# Mock database
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Versioned API",
        "versions": {
            "v1": "/api/v1",
            "v2": "/api/v2"
        }
    }
    
    
# V1 endpoints
@v1_router.get("/users", response_model=List[Dict])
async def get_users_v1():
    return [{"id": user["id"], "name": user["name"]} for user in users_db]

@v1_router.get("/users/{user_id}")
async def get_user_v1(user_id: int):
    user = next((user for user in users_db if user["id"] == user_id), None)
    if user:
        return {"id": user["id"], "name": user["name"]}
    return {"error": "User not found"}

# V2 endpoints (with additional features)
@v2_router.get("/users", response_model=List[Dict])
async def get_users_v2():
    return users_db

@v2_router.get("/users/{user_id}")
async def get_user_v2(user_id: int):
    user = next((user for user in users_db if user["id"] == user_id), None)
    if user:
        return user
    return {"error": "User not found"}

# Include routers in the main app
app.include_router(v1_router)
app.include_router(v2_router)


