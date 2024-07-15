from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI()

# 더미 유저 데이터
dummy_user = {
    "username": "testuser@example.com",
    "password": "testpassword"
}

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@app.post("/login")
async def login(request: LoginRequest):
    if request.email == dummy_user["username"] and request.password == dummy_user["password"]:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    description = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class JobListingCreate(BaseModel):
    title: str
    company: str
    description: str

class JobListingResponse(BaseModel):
    id: int
    title: str
    company: str
    description: str

    class Config:
        orm_mode = True

@app.get("/job-listings/", response_model=List[JobListingResponse])
def read_job_listings(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    job_listings = db.query(JobListing).offset(skip).limit(limit).all()
    db.close()
    return job_listings

@app.get("/job-listings/{job_id}", response_model=JobListingResponse)
def read_job_listing(job_id: int):
    db = SessionLocal()
    job_listing = db.query(JobListing).filter(JobListing.id == job_id).first()
    db.close()
    if job_listing is None:
        raise HTTPException(status_code=404, detail="Job listing not found")
    return job_listing

@app.post("/job-listings/", response_model=JobListingResponse)
def create_job_listing(job_listing: JobListingCreate):
    db = SessionLocal()
    db_job_listing = JobListing(**job_listing.dict())
    db.add(db_job_listing)
    db.commit()
    db.refresh(db_job_listing)
    db.close()
    return db_job_listing

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    if db.query(JobListing).count() == 0:
        dummy_data = [
            JobListing(title="Frontend Developer", company="Company A", description="Develop and maintain the frontend."),
            JobListing(title="Backend Developer", company="Company B", description="Develop and maintain the backend."),
            JobListing(title="Full Stack Developer", company="Company C", description="Develop and maintain both frontend and backend."),
            JobListing(title="DevOps Engineer", company="Company D", description="Manage the infrastructure and deployment."),
        ]
        db.add_all(dummy_data)
        db.commit()
    db.close()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
