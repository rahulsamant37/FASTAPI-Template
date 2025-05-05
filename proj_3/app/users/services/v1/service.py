from typing import List, Optional
from app.users.models.user import UserV1


# Mock database - in real app, you'd use a proper database
_users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]


async def get_users_v1() -> List[UserV1]:
    return [UserV1(id=user["id"], name=user["name"]) 
            for user in _users_db]
    
async def get_user_v1(user_id: int) -> Optional[UserV1]:
    user = next((user for user in _users_db if user["id"] == user_id), None)
    if user:
        return UserV1(id=user["id"], name=user["name"])
    return None