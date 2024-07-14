from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProfileCreate, Profile
from crud import create_user, create_profile
from utils.gpt import ChatGPTapi
from utils.recording import Recording
from utils.stt import OpenAIstt, ETRIstt, Googlestt
from datetime import date

router = APIRouter()


@router.post("/profile/")
async def make_profile(text: str, db: Session = Depends(get_db)):
    record_path = Recording().recording_speech()
    text = ETRIstt().run_stt(record_path)

    gpt = ChatGPTapi()
    gpt.set_messages(template_type="profile", text=text)
    answer = gpt.gpt_request()

    # extract profile
    # answer =



