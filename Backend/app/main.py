from fastapi import FastAPI

from sqlalchemy_utils import database_exists, create_database

from .database import get_rdb_session, get_mongo_database


app = FastAPI()


@app.on_event("startup")
async def startup():
    # RDB initialization
    session = get_rdb_session()
    engine = session.get_bind()
    if not database_exists(engine.url):
        create_database(engine.url)


@app.get("/hello")
def hello():
    return {"message": "hello world"}


@app.get("/sqlite_connect")
def sqlite_connect():
    return {"message": str(get_rdb_session())}


@app.get("/milvus_connect")
def milvus_connect():
    return {"message": get_mongo_database()}

