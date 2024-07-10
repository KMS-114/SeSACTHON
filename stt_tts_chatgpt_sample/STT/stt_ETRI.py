'''
ETRI AI Open API 음성인식 API 1,000건 (건당 60초 이내)/일
wav 파일 이외의 파일은 인식이 잘 안되는 오류가 있음
'''

import urllib3
import json
import base64
import time


class ETRIstt:
    def __init__(self):
        self.openApiURL = "http://aiopen.etri.re.kr:8088/WiseASR/Recognition"
        self.accesskey = ""

    def stt(self, audio_file_path):
        language_code = "korean"  # english
        file = open(audio_file_path, "rb")
        audio_contents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        request_json = {
            "argument": {
                "language_code": language_code,
                "audio": audio_contents
            }
        }

        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            self.openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": self.accesskey},
            body=json.dumps(request_json)
        )
        return response

    def run_stt(self, audio_file_path="./Data/inputAudioData/womanEng.wav"):
        print("ETRI STT run")
        start = time.time()
        response = self.stt(audio_file_path=audio_file_path)
        kor_response = str(response.data, "utf-8")
        print('ETRI STT Response : ', kor_response)

        start_point = kor_response.find('("recognized":"') + len('("recognized":"')
        stt_result = kor_response[start_point:-3]
        end = time.time()
        print(f'ETRI STT conversion time : {end - start:.3f}sec\n')

        return stt_result


if __name__ == '__main__':
    etri_stt = ETRIstt()
    answer = etri_stt.run_stt(audio_file_path="../16k.wav")
