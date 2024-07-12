from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProfileCreate, Profile
from crud import create_user
from utils.gpt import extract_in
app = FastAPI()


@app.post("/profile/", response_model=Profile)
def create_new_profile(profile: ProfileCreate, db: Session)
