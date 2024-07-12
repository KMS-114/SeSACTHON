from fastapi import FastAPI
from Backend.domain.database import Base, engine, init_db
from api.endpoints import router as api_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
init_db()
app.include_router(api_router)