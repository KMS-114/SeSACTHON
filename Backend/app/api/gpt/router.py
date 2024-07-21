from fastapi import APIRouter, Request, Query
from pydantic import BaseModel
from ...utils.gpt import ChatGPTapi

router = APIRouter(prefix="/chat")

class UserName(BaseModel):
    username:str

GRADIO_USER_NAME = None
@router.post("/set_username")
def set_gradio_username(username:UserName):
    global GRADIO_USER_NAME
    GRADIO_USER_NAME = username.username

@router.get("/get")
def set_gradio_username():
    return GRADIO_USER_NAME

@router.get("/interview")
def interview(user_profile_info: str = Query(...), question: str = Query(...)):
    gpt = ChatGPTapi()

    text = [user_profile_info, question]
    
    print(f"interview 이내 받아온 값: {text}")
    
    gpt.set_messages(template_type="interview", question=user_profile_info, answer=question)     

    profile_extract = gpt.gpt_request()
    # profile_dict = eval(profile_extract)

    return profile_extract

@router.get("/build_gradio")
def build_gradio():
    pass