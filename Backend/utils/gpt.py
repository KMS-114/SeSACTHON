from openai import OpenAI
from datetime import datetime
class ChatGPTapi:
    def __init__(self):
        # Config
        self.client = OpenAI(api_key='')
        # self.client.api_key = ''
        self.model = "gpt-3.5-turbo"
        self.template = ''
        self.prompt = ''
        self.messages = []

    def set_messages(self, template_type: str, text: str):
        if template_type in 'profile':
            self.template = {"role": "system", "content":
                ("넌 한국인이야. 너는 줄글에서 이름, 나이 등의 기본 인적 사항을 잘 분류해서 파이썬의 딕셔너리 형태로 반환하는 역할을 잘해."
                 "주어진 글에서 너가 뽑아야 할 인적사항은 'name', 'birth', 'gender', 'skills', 'careers'야"
                 "'name'은 이름을 뽑고, 'birth'는 나이나 생년월일을 통해서 XXXX-XX-XX 형태로 알려주고 나이를 알려주면 나이를 기준으로 생년 월일을 뽑아줘"
                 "2024년 기준으로 26세는 1998년생이야 이 내용을 기반으로 생년월일을 추정해야해 오늘 날짜 기준으로 해줘. 오늘은 {} 야"
                 "나이는 만나이 기준으로 하는거야"
                 "'gender'는 여성/남성으로 알려줘. 추가적으로 'skills'는 자격증으로 취득일과 취득자격증으로 만들고"
                 "'careers'는 경력사항으로 시작날짜 'startDate'와 종료날짜 'endDate'로 XXXX-XX-XX 형태, "
                 "'affiliation'은 소속된 회사를 뽑고 'summary'는 소속 회사에서 했던일 간략하게 요약한 내용을 넣어줘"
                 "'careers' key 내부엔 startDate, endDate, affiliation, summary가 표함되는거야 알겠지".format(datetime.now())
                 )}
            self.prompt = {"role": "user", "content": "아래의 줄글에서 위의 내용들을 뽑아줄래? "
                                                      "무조건 아래 자기소개 기반으로 답변을 만들어내야해 다른 답변 없이 "
                                                      "딱 파이선 딕셔너리 형태의 문자열로만 반환해줘 다른 말은 필요없어 \n\n {}".format(text)}

        elif template_type == 'Resume':
            self.template = (""
                             "")

    def gpt_request(self, history=None):
        self.messages = []

        if not history:
            self.messages.extend([self.template, self.prompt])
        else:
            self.messages.extend([self.template, history, self.prompt])

        response = self.client.chat.completions.create(
            model=self.model,
            # response_format={"type": "json_object"},
            messages=self.messages
        )
        answer = response.choices[0].message.content
        return answer

if __name__ == '__main__':
    gpt = ChatGPTapi()
    user_ans = "안녕하세요 33세 김아무개입니다 남자고 군대는 다녀왔어요. 저는 토익 700점이고 정처기 를 2021년에 땄어요 맞다 전기기사자격증도 18년도에 땄나 맞아요 땄어요. 파워포인트랑 엑셀자격증도 2010년에 땄어요. 그전엔 네모기업에서 대리로 개발 업무 진행했어요. 13년 5월 부터 17년 2월까지 일했습니다. 해양관련 레이더 개발을 진행해서 해외에 수출 진행했습니다. 세모기업도 다녔었는데 세모기업 다닌기간은 18년도 1월부터 딱 4년 다녔습니다. 거기서는 선박관련 레이더 개발 진행했습니다. 국책과제였어요"
    gpt.set_messages(template_type='profile', text=user_ans)
    answer = gpt.gpt_request()
    print(answer)



