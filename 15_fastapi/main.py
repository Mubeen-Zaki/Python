from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdate
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("1f0c4a08-1793-457c-ae4d-058b75ee2b7c"), 
        first_name="Md",
        last_name="Siraj",
        gender=Gender.male, 
        role=[Role.student]
    ),
    User(
        id=UUID("37e12680-f7e4-4bae-8546-af2642c61944"), 
        first_name="Alex",
        last_name="Sem",
        gender=Gender.female, 
        role=[Role.student, Role.user]
    )
]

@app.get("/")
async def root():
    return {"hello" : "world"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for item in db:
        if id == item.id:
            db.remove(item)
            return "User removed successfully"
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {id} does not exist!"
    )

@app.put("/api/v1/users/{id}")
async def update_user(id: UUID, user_update: UserUpdate):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.role is not None:
                user.role = user_update.role
            if user_update.gender is not None:
                user.gender = user_update.gender
            return "User details updated Successfully!"
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {id} does not exist!"
    )
            