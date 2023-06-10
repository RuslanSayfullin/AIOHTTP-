from fastapi import FastAPI, depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

def verify_user(credentials: HTTPBasicCredentials):
    # Проверяет имя пользователя и пароль
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    verify_user(credentials)
    return {"message": "Login successful."}

@app.get("/protected")
async def protected_endpoint(credentials: HTTPBasicCredentials = Depends(security)):
    verify_user(credentials)
    return {"message": "Access granted."}
