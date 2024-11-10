from fastapi import FastAPI, HTTPException, Path, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.templating import Jinja2Templates


app = FastAPI()

users = []

templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    id: int
    username: str
    age: int




@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
def get_by_userid(request: Request, user_id: int) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example="UrbanUser")],
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    if users:
        new_id = users[-1].id + 1
    else:
        new_id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example="UrbanUser")],
                      user_id: int = Path(ge=1, le=100, description="Enter USER ID", example='31'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i].username = username
            users[i].age = age
            return users[i]
    raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
def delete_user(user_id: int = Path(ge=1, le=100, description="Enter USER ID", example='31')):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")

