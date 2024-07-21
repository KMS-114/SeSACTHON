from typing import Optional

from openai import OpenAI
from datetime import datetime


class ChatGPTapi:
    def __init__(self):
        # Config
        self.client = OpenAI(api_key="")
        # self.client.api_key = ''
        self.model = "gpt-3.5-turbo"
        self.template = ""
        self.prompt = ""
        self.messages = []

    def set_messages(self, template_type: str, question: Optional[str], answer: str):
        if template_type in "profile":
            self.template = {
                "role": "system",
                "content": (
                    "넌 한국인이야. 너는 줄글에서 이름, 나이 등의 기본 인적 사항을 잘 분류해서 파이썬의 딕셔너리 형태로 반환하는 역할을 잘해."
                    "주어진 글에서 너가 뽑아야 할 인적사항은 'name', 'birth', 'gender', 'skills', 'careers'야."
                    "'name'은 이름을 뽑고, 'birth'는 나이나 생년월일을 통해서 XXXX-XX-XX 형태로 알려주고 나이를 알려주면 나이를 기준으로 생년 월일을 뽑아줘"
                    "2024년 기준으로 26세는 1998년생이야 이 내용을 기반으로 생년월일을 추정해야해 오늘 날짜 기준으로 해줘. 오늘은 {} 야"
                    "나이는 만나이 기준으로 하는거야"
                    "'gender'는 남성은 1 여성은 2로 알려줘. 추가적으로 'skills'는 자격증 이름을 뽑아서 문자열 리스트 형태로 만들어서 넣어줘"
                    "'careers'는 경력사항으로 시작날짜 'startDate'와 종료날짜 'endDate'로 XXXX-XX-XX 형태, "
                    "'affiliation'은 소속된 회사를 뽑고 'summary'는 소속 회사에서 했던일 간략하게 요약한 내용을 넣어줘"
                    "'careers' key 내부엔 startDate, endDate, affiliation, summary가 표함되는거야 알겠지".format(
                        datetime.now()
                    )
                ),
            }
            self.prompt = {
                "role": "user",
                "content": (
                    "아래의 줄글에서 위의 내용들을 뽑아줄래? "
                    "무조건 아래 자기소개 기반으로 답변을 만들어내야해 다른 답변 없이 "
                    "딱 파이선 딕셔너리 형태의 문자열로만 반환해줘 다른 말은 필요없어 \n\n {}".format(
                        answer
                    )
                ),
            }

        elif template_type == "interview":
            text = []
            text.append(question)
            text.append(answer)

            print(f"text[0]: {text[0]}")
            print(f"text[1]: {text[1]}")

            self.template = {
                "role": "system",
                "content": (
                    "너는 한국인이고, 면접장에서 면접을 보고 있는 구직자이다."
                    "너의 신상 정보는 'name', 'birth', 'gender'로 나타나있다."
                    "너의 경력 정보는 'skills', 'careers'로 나타나있다."
                    "너에게 주어졌던 질문과 그에 대한 대답은 'coverLetterQuestion', 'content'로 나타나있다."
                    "다음은 너의 실제 정보이다. \n {}".format(
                        text[0]
                    )
                ),
            }

            self.prompt = {
                "role": "user",
                "content": (
                    "아래의 질문은 면접자가 너한테 질문하는 내용이야. 질문에 대해 구직자 입장에서 답변해봐 \n\n {}".format(text[1])
                ),
            }

        elif template_type == "resume":
            self.template = {
                "role": "system",
                "content": (
                    f"넌 한국인이야. 지금 너가 하는 일은 자소서를 잘 정리하고 만들어서 자소서를 작성해주는 역할을 할거야."
                    f"너는 아래 주어진 글에서 {question}의 의도에 잘 맞게 답변을 생성해줘야해. "
                    f"누가봐도 합격할만하게 자소서를 정리, 만들어주는데 절대로 진짜 절대로 거짓말을 섞거나 글과 다른 내용을 작성하면 안돼"
                    f"거짓 내용은 절대 안되고 아래의 글 기반으로 만들어야해."
                ),
            }
            self.prompt = {
                "role": "user",
                "content": (
                    f"아래의 줄글에서 자소서 문항에 대한 답변을 만들어줄래? "
                    f"무조건 아래 자기소개 기반으로 답변을 만들어내야해 다른 답변 없이 "
                    f"딱 문자열로만 반환해줘 다른 말은 필요없어 \n\n {answer}"
                ),
            }
    def gpt_request(self, history=None):
        self.messages = []

        if not history:
            self.messages.extend([self.template, self.prompt])
        else:
            self.messages.extend([self.template, history, self.prompt])

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
        )
        gpt_answer = response.choices[0].message.content
        return gpt_answer



if __name__ == "__main__":
    gpt = ChatGPTapi()
    user_ans = "안녕하세요 33세 김아무개입니다 7월 3일에 태어났어요 남자고 군대는 다녀왔어요. 저는 토익 700점이고 정처기 를 2021년에 땄어요 맞다 전기기사자격증도 18년도에 땄나 맞아요 땄어요. 파워포인트랑 엑셀자격증도 2010년에 땄어요. 그전엔 네모기업에서 대리로 개발 업무 진행했어요. 13년 5월 부터 17년 2월까지 일했습니다. 해양관련 레이더 개발을 진행해서 해외에 수출 진행했습니다. 세모기업도 다녔었는데 세모기업 다닌기간은 18년도 1월부터 딱 4년 다녔습니다. 거기서는 선박관련 레이더 개발 진행했습니다. 국책과제였어요"
    gpt.set_messages(template_type="profile", text=user_ans)
    answer = gpt.gpt_request()
    print(answer)
    answer_dict = eval(answer)
    print(answer_dict)
    print(type(answer_dict))