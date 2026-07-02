from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    email: str
    password: str
class UserResponse(BaseModel):
    name: str
    email: str
    full_name: str


@app.get("/users/", response_model=UserResponse)
async def get_user(user: User):
    return UserResponse(name=user.name, email=user.email, full_name=f"{user.name} <{user.email}>")


# store user data in memory
@app.post("/users/", response_model=UserResponse)
async def create_user(user: User):
    users.append(user)
    return UserResponse(name=user.name, email=user.email, full_name=f"{user.name} <{user.email}>")