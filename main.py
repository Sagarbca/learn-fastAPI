from fastapi import FastAPI,Request
from pydantic import BaseModel
import time
app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, call_next):
    # Code to execute before the request is processed
    start_time = time.time()
    print("Before request")
    
    response = await call_next(request)
    
    # Code to execute after the request is processed
    end_time = time.time()
    print(f"After request: {end_time - start_time} seconds")
    
    return response