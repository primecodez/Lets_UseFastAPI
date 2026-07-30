from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to this Server!"}

@app.get("/about")
def about():
    return {"info": "This is my API"}

@app.get("/contact")
def contact():
    return {"email": "test@gmail.com"}

@app.get("/services")
def services():
    return{"services": ["Web Development", "App Development", "SEO Optimization"]}

