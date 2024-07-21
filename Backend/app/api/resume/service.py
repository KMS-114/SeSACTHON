from fastapi import UploadFile

from ...utils.gpt import ChatGPTapi
from ...utils.stt import ETRIstt
from ...utils.utils import save_upload_file

stt = ETRIstt()

async def generate_resume(username: str, question: List[str], file: UploadFile):
    gpt = ChatGPTapi()

    file_path = save_upload_file(username, file, "resume")
    user_answer = stt.run_stt(file_path)

    gpt.set_messages(template_type="resume", question=question, answer=user_answer)
    resume_refactor = gpt.gpt_request()
    return resume_refactor
