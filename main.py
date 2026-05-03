from fastapi import FastAPI

app = FastAPI()
users= {}
@app.post


@app.get("/")
def home():
    return {"message": "Hello world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None, name: str | None = None):
    return {"item_id": item_id, "q": q, "name": name}