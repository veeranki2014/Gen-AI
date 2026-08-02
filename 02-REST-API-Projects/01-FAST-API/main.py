from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def get_welcome_message():
    return {"message" : "Welcome to FastAPI"}

@app.get("/greeting")
def get_greet_message():
    return {"message" : "Hello World"}

