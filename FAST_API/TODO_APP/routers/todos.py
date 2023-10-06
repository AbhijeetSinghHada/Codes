from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, status
import models
from database import SessionLocal
from .auth import get_current_user
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/")
async def read_all(db: db_dependency):
    user = await get_current_user()
    print(user)
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return db.query(models.Todos).filter(models.Todos.owner_id == user.get("user_id")).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_by_id(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    data = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(
        models.Todos.owner_id == user.get("user_id")).first()
    if data is not None:
        return data
    raise HTTPException(status_code=404, detail="Todo Not Found")


@router.post("/todo/", status_code=status.HTTP_201_CREATED)
async def create_todo_item(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    todo_model = models.Todos(
        **todo_request.model_dump(), owner_id=user.get('user_id'))

    db.add(todo_model)
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo_item(user: user_dependency, db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):

    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    todo_model = db.query(models.Todos).filter(
        models.Todos.id == todo_id).filter(
        models.Todos.owner_id == user.get("user_id")).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    todo_model.title = todo_request.title  # type: ignore
    todo_model.description = todo_request.description  # type: ignore
    todo_model.priority = todo_request.priority  # type: ignore
    todo_model.complete = todo_request.complete  # type: ignore

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):

    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    todo_request = db.query(models.Todos).filter(
        models.Todos.id == todo_id).filter(
        models.Todos.owner_id == user.get("user_id")).first()
    if not todo_request:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    db.query(models.Todos).filter(models.Todos.id == todo_id).filter(
        models.Todos.owner_id == user.get("user_id")).delete()
    db.commit()
