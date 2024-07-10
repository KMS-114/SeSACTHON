from openai import OpenAI
import json
import time


class ChatGPTapi:
    def __init__(self):
        # Config
        self.client = OpenAI()
        self.client.api_key = ''
        self.client.organization = ''

        self.model = "gpt-3.5-turbo"
        self.questions = []

    def do_single_chat(self, question="What is your name"):
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message.content
        return answer

    def do_chat(self, question="What is your name", history=[]):
        history.append({"role": "user", "content": question})
        print('history: ', history)
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=history
        )
        answer = response.choices[0].message.content
        return answer, history

    def extract_answer(self, completion):
        result_json = json.load(str(completion.choices[0]))
        print('Json result : ', result_json)

        result_content = result_json['message']['content']
        return result_content


if __name__ == '__main__':
    start = time.time()
    chatgpt = ChatGPTapi()
    answer, history = chatgpt.do_chaat('안녕하세요')

    end = time.time()
    print(end - start)
    print(answer)

    start = time.time()
    chatgpt = ChatGPTapi()
    answer, history = chatgpt.do_chat('안녕하세요')

    end = time.time()
    print(end - start)
    print(answer)
