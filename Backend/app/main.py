from fastapi import FastAPI, Form
from starlette.middleware.cors import CORSMiddleware

from .api.job_posting.router import router as job_posting_router
from .api.profile.router import router as profile_router
from .api.resume.router import router as resume_router
from .api.user.router import router as user_router


app = FastAPI()
app.include_router(job_posting_router)
app.include_router(profile_router)
app.include_router(resume_router)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     # RDB initialization
#     session = SessionLocal()
#     engine = session.get_bind()
#     if not database_exists(engine.url):
#         create_database(engine.url)

@app.post("/login")
async def login(email: str = Form(), password: str = Form()):
    print(f"Email: {email}")
    print(f"Password: {password}")
    return {"message": "Login data received"}

@app.get("/hello")
def hello():
    return {"message": "hello world"}


