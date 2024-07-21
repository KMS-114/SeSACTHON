import gradio as gr
import requests
from typing import List, Dict

USER_PROFILE_INFO = None
USER_NAME = None

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
    username = requests.get("http://localhost:8000/chat/get")
    username = username.json()

    params={
        'username': username        # svelte에서 넘긴 usrname 사용하려면 USER_NAME으로 대체
    }
    response = requests.get(f"http://localhost:8000/profile/get", params=params)
    USER_PROFILE_INFO = response.json()
    print(f"username({username})으로 가져온 USER_PROFILE_INFO: {USER_PROFILE_INFO}")

    user_profile_info = USER_PROFILE_INFO
    user_profile_info = str(user_profile_info)  # dict -> str로 변경.
                                                # dict 자체를 쿼리 매개변수로 보내기 어려움. 다른 전처리 해야함
    params = {
        'user_profile_info': user_profile_info,
        'question': question
    }

    interviewer_answer = requests.get("http://localhost:8000/chat/interview", params=params)
    
    return interviewer_answer.json()

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

    # gr.Interface(
    #     fn=get_user_info_by_user_name,
    #     inputs="text",
    #     outputs="text",    
    #     title="Number Processing Interface",
    #     description="Enter a number and the server will process it."
    # )

    gr.Interface(
        fn=chat_with_api,
        inputs="text",
        outputs="text",
        title="유저 이력서 및 프로필 정보에 기반한 가상면접",
        description="Send a message and get a response from the FastAPI server."
    )

if __name__ == "__main__":
    # USER_NAME = requests.get("http://localhost:8000/chat/get_username")
    iface.launch()