from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_users(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    max_key = max(int(key) for key in users.keys())
    new_user_id = str(max_key + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      user_id: int = Path(ge=1, le=100, description="Enter USER ID", example='31'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter USER ID", example='31')):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[str(user_id)]
    return f"User {user_id} is deleted"
