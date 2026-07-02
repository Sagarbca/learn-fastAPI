from fastapi import FastAPI, status, HTTPException,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

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

#optional routes
@app.get("/items")
async def get_items(item : str = "None"):
    return {"item": item}


#default route
@app.get("/products")
async def get_products(limit : int = 10):
    return {"products": ["Product 1", "Product 2", "Product 3"], "limit": limit}

#multiple query parameters
@app.get("/productsWithLimitOffset")
async def get_products(limit : int = 10, offset : int = 0):
    return {"products": ["Product 1", "Product 2", "Product 3"], "limit": limit, "offset": offset}


#handle pydantic and post route
@app.post("/create_user")
def create_user(name: str, age: int):
    return {"message": "User created", "user": {"name": name, "age": age}}


@app.post("/create_user_with_json")
def create_user_pydantic(user: dict):
    return {"message": "User created", "user": user}

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address


@app.post("/create_user_with_pydantic_model")
def create_user_with_pydantic(user: User, status_code: int = status.HTTP_201_CREATED):
    return {"message": "User created", "user": user}


@app.get("/userById/{user_id}")
def get_user_by_id(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    return {"user_id": user_id, "name": f"User {user_id}"}



class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id


@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"User with ID {exc.user_id} not found."},
    )