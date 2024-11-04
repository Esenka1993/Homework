from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
async def user_inf(username: str, age: int) -> dict:
    return {f"Информация о пользовател. {username}": f'{age}'}

@app.get("/user/{user_id}")
async def id_f(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь №{user_id}'}

@app.get("/user/admin")
async def admin_f() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/")
async def welcome() -> dict:
    return {'message': "Главная страница"}




