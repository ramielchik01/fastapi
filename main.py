from fastapi import FastAPI

app = FastAPI()
users= {}
@app.post("/register")
def register(username: str, password: str):
    if username in users:
        return{"error":"Username already exict"}
    users[username] = password
    return{"message":"Registered succesfull"}
@app.post("/login")
def login(username: str, password: str):
    if username not in users:
        return{"error":"user is not found"}
    if users[username] != password:
        return{"message":"password is not correct"}
    return{"message": "you loged in succesfully"}