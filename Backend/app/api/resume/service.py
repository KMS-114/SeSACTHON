from fastapi import UploadFile

from ...utils.gpt import ChatGPTapi
from ...utils.stt import ETRIstt
from ...utils.utils import save_upload_file

stt = ETRIstt()

async def generate_resume(username: str, question: list[str], file: UploadFile):
    gpt = ChatGPTapi()

    file_path = await save_upload_file(username=username, file=file, type="resume")
    user_answer = stt.run_stt(file_path=file_path)

    gpt.set_messages(template_type="resume", question=question, answer=user_answer)
    resume_refactor = gpt.gpt_request()
    resume_list = eval(resume_refactor)
    return resume_list

async def generate_resume_test(username: str, question: list[str], answer: str):
    gpt = ChatGPTapi()

    gpt.set_messages(template_type="resume", question=question, answer=answer)
    resume_refactor = gpt.gpt_request()
    resume_list = eval(resume_refactor)
    return resume_list