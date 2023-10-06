from fastapi import FastAPI, Depends
import models
from database import engine
from routers import auth, todos
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.route("/")
def home(request):
    return RedirectResponse("/todos", status_code=status.HTTP_302_FOUND)


app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(auth.router)
app.include_router(todos.router)
