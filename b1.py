from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/about")
def about():
    return {"info": "This is my API"}

@app.get("/contact")
def contact():
    return {"email": "test@gmail.com"}