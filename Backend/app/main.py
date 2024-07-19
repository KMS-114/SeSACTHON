from fastapi import FastAPI

from api.job_posting.router import router as job_posting_router
from api.profile.router import router as profile_router
from api.resume.router import router as resume_router
from api.user.router import router as user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(job_posting_router)
app.include_router(profile_router)
app.include_router(resume_router)
app.include_router(user_router)


# @app.on_event("startup")
# async def startup():
#     # RDB initialization
#     session = SessionLocal()
#     engine = session.get_bind()
#     if not database_exists(engine.url):
#         create_database(engine.url)

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"message": "hello world"}
