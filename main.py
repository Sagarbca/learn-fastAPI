from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"Hello": "World"}

#about
@app.get("/about")
async def about():
    return {"About": "This is a FastAPI application."}


#users
@app.get("/users")
async def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}


#dynamic users route
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}