from fastapi import FastAPI,depends, HTTPException,Header

app = FastAPI()

def common_logic():
    return {
        "message": "This is a common logic function that can be reused across multiple endpoints."
    }

@app.get("/home")
def read_home(data = depends(common_logic)):
    return data 

def get_current_user():
    return {"user": "John Doe"}

@app.get("/profile")
def read_profile(current_user = depends(get_current_user)):
    return {"message": f"Hello, {current_user['user']}! This is your profile."}

@app.get("/dashboard")
def dashboard(current_user = depends(get_current_user)):
    return {"message": f"Hello, {current_user['user']}! This is your dashboard."}

def verify_token(token: str = Header(None)):
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": "John Doe"}

@app.get("/secure-data")
def read_secure_data(current_user = depends(verify_token)):
    return {"message": f"Hello, {current_user['user']}! This is your secure data."}