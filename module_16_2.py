from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{username}/{age}'")
async def user_inf(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> dict:
    return {f"Информация о пользователе. {username}": f'{age}'}

@app.get("/user/{user_id}")
async def id_f(user_id: int =Path(ge=1, le=100, description="Enter USER ID", example='31')) -> dict:
    return {'message': f'Вы вошли как пользователь №{user_id}'}

@app.get("/user/admin")
async def admin_f() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/")
async def welcome() -> dict:
    return {'message': "Главная страница"}
