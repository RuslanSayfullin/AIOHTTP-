from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

def vverify_user(credentials: HTTPBasicCredentials):
    # Проверяем имя пользователя и пароль 
    if predential.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    verify_user(credentials)
    return{"message": "Login seccessful."}

@app.get("/protected")
async def protected_endpoint(credentials: HTTPBasicCredentials = Depends(security)):
    verify_user(credentials)
    return {"messge": "Access granted."}
