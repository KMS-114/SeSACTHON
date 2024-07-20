from _datetime import datetime
import os
import shutil
from typing import Union

from fastapi import UploadFile

from .repository import create_profile_document
from .schema import ProfileModel
from ...utils.gpt import ChatGPTapi
from ...utils.stt import ETRIstt

stt = ETRIstt()


async def refactoring_profile_with_mp3(username: str, file:UploadFile):
    gpt = ChatGPTapi()

    file_path = await save_upload_file(username, file)
    user_answer = stt.run_stt(file_path)

    gpt.set_messages(template_type="profile", text=user_answer)
    profile_extract = gpt.gpt_request()
    profile_dict = eval(profile_extract)

    profile_save = await convert_to_datetime(profile_dict)
    profile_save['username'] = username

    profile = ProfileModel(**profile_save)
    return profile

async def refactoring_profile_with_text(username: str, content:str):
    gpt = ChatGPTapi()

    # file_path = await save_upload_file(username, file)
    # user_answer = stt.run_stt(file_path)

    gpt.set_messages(template_type="profile", text=content)
    profile_extract = gpt.gpt_request()
    profile_dict = eval(profile_extract)

    profile_save = await convert_to_datetime(profile_dict)
    profile_save['username'] = username

    profile = ProfileModel(**profile_save)
    return profile

async def save_upload_file(username: str, audio: UploadFile):
    save_path = f"../../data/uploadedFiles/{username}"
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, audio.filename)
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(audio.file, file_object)
    return file_path


async def convert_to_datetime(obj):
    if isinstance(obj, list):
        for career in obj:
            await convert_to_datetime(career)
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'startDate' or key == 'endDate' or key == "birth":
                obj[key] = datetime.strptime(value, "%Y-%m-%d")
            elif isinstance(value, (list, dict)):
                await convert_to_datetime(value)

    return obj

async def refactoring_profile_test(username: str):
    gpt = ChatGPTapi()

    user_answer = "안녕하세요 33세 김아무개입니다 7월 3일에 태어났어요 남자고 군대는 다녀왔어요. 저는 토익 700점이고 정처기 를 2021년에 땄어요 맞다 전기기사자격증도 18년도에 땄나 맞아요 땄어요. 파워포인트랑 엑셀자격증도 2010년에 땄어요. 그전엔 네모기업에서 대리로 개발 업무 진행했어요. 13년 5월 13일부터 17년 2월 17일까지 일했습니다. 해양관련 레이더 개발을 진행해서 해외에 수출 진행했습니다. 세모기업도 다녔었는데 세모기업 다닌기간은 18년도 1월 16일부터 딱 4년 다녔습니다. 거기서는 선박관련 레이더 개발 진행했습니다. 국책과제였어요"
    # print(user_answer)
    gpt.set_messages(template_type="profile", text=user_answer)
    profile_extract = gpt.gpt_request()
    profile_dict = eval(profile_extract)
    profile_save = await convert_to_datetime(profile_dict)
    profile_save['username'] = username
    print(profile_save)
    profile = ProfileModel(**profile_save)

    # print(profile)
    # await create_profile_document(profile_save)
    return profile

async def create_profile_test(profile: ProfileModel):
    print(profile)
    response = await create_profile_document(profile)
    print(response)
    return response
