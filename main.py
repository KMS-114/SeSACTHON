from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import Backend.models
from Backend.database import engine

# 자동 테이블 생성
Backend.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",    # 또는 "http://localhost:5173"
]

from Backend.domain.board import board_router
from Backend.domain.user import user_router

app.include_router(board_router.app, tags=["board"])
app.include_router(user_router.app, tags=["user"])

@app.get("/")
def read_root():
    return {"Hello": "World"}