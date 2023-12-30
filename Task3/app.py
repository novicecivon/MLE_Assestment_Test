from mangum import Mangum
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def home():
    return "Hello World"


@app.post("/webhook")  # Use @app.post for POST requests
async def webhook(request: Request):
    req = await request.json()  # Get JSON data asynchronously
    return req


handler = Mangum(app)
