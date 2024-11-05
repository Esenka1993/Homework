from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def get_all_users() -> List:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example="UrbanUser")],
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    if users:
        new_id = users[-1].id + 1
    else:
        new_id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example="UrbanUser")],
                      user_id: int = Path(ge=1, le=100, description="Enter USER ID", example='31'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i].username = username
            users[i].age = age
            return users[i]
    raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter USER ID", example='31')):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")