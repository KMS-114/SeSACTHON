from fastapi import APIRouter, Request, Query
from ...utils.gpt import ChatGPTapi

router = APIRouter(prefix="/chat")

# @router.post("/chat")
# def chat(question:str, interviewee_answer:str):
#     chatgpt_api = ChatgptAPI(api_key="")
#     prompt = "너한테 2개의 입력을 줄게. 자기소개서 문항, 면접자의 음성 답변이야. 면접자의 음성 답변을 문어체로 바꿔서 자기소개서 질문에 대한 답변을 작성해줘\n"
#     # prompt += "자기소개서 문항: 개발자로서의 성장 과정을 자세히 설명해주세요."
#     prompt += question + "\n"
#     # prompt += "면접자의 음성 답변: 안녕하세요. 제 이름은 양호준 입니다. 제가 개발자로 성장한 과정은 다사다난 했어요. 바야흐로 대학교 2학년 때부터였죠. 네이버 부스트 캠프 AI 6기에 당당히 합격해, 웹 개발과 프론트 개발을 모두 경험하며 성장했어요. 특히, 1초당 5000개 이상의 데이터를 DB에 저장하는 문제를 겪고 해결함으로써 병렬 처리 기술의 기초를 닦았답니다."
#     prompt += interviewee_answer + "\n"

#     chatgpt_api.set_prompt(prompt)
#     return chatgpt_api.get_answer()


# @router.post("/chat")
# async def chat(request: Request):
#     data = await request.json()
#     q = data.get('chat_text')
#     # a = data.get('answer')

#     chatgpt_api = ChatgptAPI(api_key="")
#     prompt = "너한테 2개의 입력을 줄게. 자기소개서 문항, 면접자의 음성 답변이야. 면접자의 음성 답변을 문어체로 바꿔서 자기소개서 질문에 대한 답변을 작성해줘\n"
#     # prompt += "자기소개서 문항: 개발자로서의 성장 과정을 자세히 설명해주세요."
#     prompt += q + "\n"
#     # prompt += "면접자의 음성 답변: 안녕하세요. 제 이름은 양호준 입니다. 제가 개발자로 성장한 과정은 다사다난 했어요. 바야흐로 대학교 2학년 때부터였죠. 네이버 부스트 캠프 AI 6기에 당당히 합격해, 웹 개발과 프론트 개발을 모두 경험하며 성장했어요. 특히, 1초당 5000개 이상의 데이터를 DB에 저장하는 문제를 겪고 해결함으로써 병렬 처리 기술의 기초를 닦았답니다."
#     # prompt += a + "\n"

#     chatgpt_api.set_prompt(prompt)
    
#     response = chatgpt_api.get_answer()
#     response = {"response": response}
#     return response

@router.get("/interview")
def interview(user_info: str = Query(...), question: str = Query(...)):
    gpt = ChatGPTapi()

    text = [user_info, question]
    print(text)
    
    gpt.set_messages(template_type="interview", question=user_info, answer=question)     

    profile_extract = gpt.gpt_request()
    # profile_dict = eval(profile_extract)

    return profile_extract