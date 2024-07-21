import gradio as gr
import requests
from typing import List, Dict

USER_INFO = None

# DB에서 이력서 정보를 가져오는 함수
def get_resume_info():
    # 실제 DB 호출 대신 예제 데이터를 반환합니다.
    resume_info = """
    <h3>Resume Information</h3>
    <p><strong>Name:</strong> John Doe</p>
    <p><strong>Experience:</strong> 5 years in software development</p>
    <p><strong>Skills:</strong> Python, JavaScript, SQL</p>
    <p><strong>Education:</strong> B.Sc. in Computer Science</p>
    """
    return resume_info

# FastAPI와 통신하여 채팅 응답을 받는 함수
def chat_with_api(question:str):
    # TODO
    # user_info 구현
    user_info = USER_INFO
    print(f"user_info: {user_info}, type(): {type(user_info)}")

    params = {
        'user_info': user_info,
        'question': question
    }

    interviewer_anser = requests.get("http://localhost:8000/chat/interview", params=params)
    print(f"inerview_answer.json(): {interviewer_anser.json()}")
    
    return interviewer_anser.json()
    

def get_user_info_by_user_name(username):
    global USER_INFO    

    # requests.get("http:localhost:8000/job_posting/detail/669bff912ffd2cca659e62e0")
    response = requests.get(f"http://localhost:8000/user/get/{username}")
    USER_INFO = response.json()
    print(f"USER_INFO: {USER_INFO}")
    return response.json()

def get_user_profile() -> List[Dict]:

    response = requests.get("http://localhost:8000/job_posting/all")
    job_posting_list = response.json().get('jobPostings')
    return job_posting_list

# 버튼 클릭 시 userId를 텍스트박스에 출력하는 함수
def display_user_id(user_id):
    return user_id

# 이력서 정보를 가져오는 버튼 클릭 이벤트와 함수 연결
def show_resumes():
    resume_list = get_user_profile()
    update_show = [gr.Button(visible=True, value=resume["username"]) for resume in resume_list]
    update_hide = [gr.Button(visible=False, value="") for _ in range(10 - len(resume_list))]
    return update_show + update_hide

# 이력서 정보를 텍스트 블록으로 표시하고, 채팅 기능을 추가하는 인터페이스 정의
resume_info = get_resume_info()
iface = gr.Blocks()

btn_list = []

with iface:
    with gr.Row():
        for i in range(10):
            btn = gr.Button(visible=False)
            btn_list.append(btn)

    # gr.HTML(resume_info)  # 이력서 정보 표시

    resume_output = gr.Textbox(lines=10, label="Resume Details")

    # "이력서 정보 불러오기" 버튼 생성 및 클릭 이벤트 연결
    # fetch_button = gr.Button("이력서 정보 불러오기")
    # fetch_button.click(show_resumes, inputs=None, outputs=btn_list)

    # 각 버튼 클릭 시 userId 출력하는 함수와 연결
    for btn in btn_list:
        btn.click(display_user_id, inputs=btn, outputs=resume_output)

    gr.Interface(
        fn=get_user_info_by_user_name,
        inputs="text",
        outputs="text",    
        title="Number Processing Interface",
        description="Enter a number and the server will process it."
    )

    gr.Interface(
        fn=chat_with_api,
        inputs="text",
        outputs="text",
        title="유저 이력서 및 프로필 정보에 기반한 가상면접",
        description="Send a message and get a response from the FastAPI server."
    )

if __name__ == "__main__":
    iface.launch()
