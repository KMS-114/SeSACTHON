"""
ETRI AI Open API 음성인식 API 1,000건 (건당 60초 이내)/일
wav 파일 이외의 파일은 인식이 잘 안되는 오류가 있음
"""

import os

import urllib3
import json
import base64
import time
from google.cloud import speech

from openai import OpenAI


class ETRIstt:
    def __init__(self):
        self.openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
        self.accesskey = ""

    def stt(self, audio_file_path):
        language_code = "korean"  # english
        file = open(audio_file_path, "rb")
        audio_contents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        request_json = {
            "argument": {"language_code": language_code, "audio": audio_contents}
        }

        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            self.openApiURL,
            headers={
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": self.accesskey,
            },
            body=json.dumps(request_json),
        )
        return response

    def run_stt(self, audio_file_path="../data/recordingData/20240712_221523.wav"):
        response = self.stt(audio_file_path=audio_file_path)
        response_data = response.data.decode("utf-8")
        response_parsed = json.loads(response_data)
        answer = response_parsed.get("return_object", {}).get("recognized", "")
        return answer


class OpenAIstt:
    def __init__(self):
        # config
        self.client = OpenAI()
        self.client.api_key = ""

    def run_stt(self, audio_file_path="../Data/recordingData/womanEng.wav"):
        audiofile = open(audio_file_path, "rb")
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1", file=audiofile, response_format="text"
        )
        print(transcript)

        result = json.loads(str(transcript))["text"]
        return result


class Googlestt:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
            "stt-to-gpt-to-tts-9c93e4bf4ea7.json"
        )

    def run_stt(self, audio_file_path="./data/inputAudioData/womanEng.wav"):
        # instantiates a client
        print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

        client = speech.SpeechClient()

        gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
        audio = speech.RecognitionAudio(uri=gcs_uri)

        config = speech.RecognitionConfig(
            encodings=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))


if __name__ == "__main__":
    etri_stt = ETRIstt()
    answer = etri_stt.run_stt(
        audio_file_path="../data/recordingData/20240712_221900.wav"
    )
    print(answer)
