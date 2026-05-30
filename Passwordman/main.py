from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Load existing passwords
try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = {}


# Pydantic Model
class PasswordData(BaseModel):
    site: str
    password: str


# Save helper
def save_passwords():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)


# CREATE
@app.post("/passwords")
def add_password(data: PasswordData):
    passwords[data.site] = data.password
    save_passwords()

    return {
        "message": "Password saved successfully!"
    }


# READ ALL
@app.get("/passwords")
def view_passwords():
    return passwords


# READ ONE
@app.get("/passwords/{site}")
def get_password(site: str):

    if site not in passwords:
        return {"error": "Site not found"}

    return {
        "site": site,
        "password": passwords[site]
    }


# DELETE
@app.delete("/passwords/{site}")
def delete_password(site: str):

    if site not in passwords:
        return {"error": "Site not found"}

    del passwords[site]
    save_passwords()

    return {
        "message": f"{site} deleted successfully"
    }