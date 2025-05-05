from fastapi import FastAPI
from typing import List, Dict

app = FastAPI(title="Problematic API Example")

# Mock database
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]


@app.get("/v1/api/users", response_model=List[Dict])
async def get_users():
    return [{"id": user["id"], "name": user["name"]} for user in users_db]
    # But what if we need to modify it to include email? 
    
@app.get("/v2/api/users", response_model=List[Dict])
async def get_users():
    return [{"id": user["id"], "name": user["name"], "email": user["email"]} for user in users_db]



@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    user = next((user for user in users_db if user["id"] == user_id), None)
    if user:
        return {"id": user["id"], "name": user["name"]}
        # Again, we can't just add email without breaking existing clients
    return {"error": "User not found"}
