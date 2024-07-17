from _datetime import datetime
import os
import shutil

from fastapi import UploadFile

from .repository import create_profile_document
from ...utils.gpt import ChatGPTapi
from ...utils.stt import ETRIstt

stt = ETRIstt()


def create_profile(userId: str, file: UploadFile):
    gpt = ChatGPTapi()

    file_path = save_upload_file(userId, file)
    user_answer = stt.run_stt(file_path)

    profile_extract = gpt.set_messages(template_type="profile", text=user_answer)
    profile_dict = eval(profile_extract)

    profile_save = convert_to_datetime(profile_dict)
    create_profile_document(profile_save)

def save_upload_file(userId: str, audio: UploadFile):
    save_path = f"../../data/uploadedFiles/{userId}"
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, audio.filename)
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(audio.file,file_object)
    return file_path


def convert_to_datetime(obj):
    if isinstance(obj, list):
        for career in obj:
            convert_to_datetime(career)
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'startDate' or key == 'endDate' or key == "birth":
                obj[key] = datetime.strptime(value, "%Y-%m-%d")
            elif isinstance(value, (list, dict)):
                convert_to_datetime(value)

    return obj