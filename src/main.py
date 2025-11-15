from contextlib import asynccontextmanager


from fastapi import FastAPI
from src.database import init_db
from src.users.router import users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(
    router=users_router
)