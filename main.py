from fastapi import FastAPI
from pydantic import BaseModel

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
def create_user_with_pydantic(user: User):
    return {"message": "User created", "user": user}


#add Todo applocation

todos = []
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool


#add todo route
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created", "todo": todo}


#get all todos
@app.get("/todos")
def get_todos():
    return {"todos": todos}


#getById
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}

#updateTodos
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = todo
            return {"message": "Todo updated", "todo": todo}
    return {"message": "Todo not found"}


#deleteTodos
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}



#addTodos withmultipleQueryParameters
@app.post("/todosWithQueryParameters")
def todos_with_query_parameters(todo : Todo):
     todos.append(todo)
     return {"message": "Todo created", "todo": todo}


#updateTodos withmultipleQueryParameters
@app.put("/todosWithQueryParameters/{todo_id}")
def update_todos_with_query_parameters(todo_id: int, todo: Todo, completed: bool = False):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = todo
            return {"message": "Todo updated", "todo": todo, "completed": completed}
    return {"message": "Todo not found"}