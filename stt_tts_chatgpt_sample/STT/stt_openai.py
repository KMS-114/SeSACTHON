import openai
from openai import OpenAI
import json
import time


class OpenAIstt:
    def __init__(self):
        # config
        self.client = OpenAI()
        self.OpenAI_key = ''
        self.OpenAI_Organization = ''

        self.client.api_key = self.OpenAI_key
        self.client.api_key = self.OpenAI_Organization


    def run_stt(self, audio_file_path='../Data/inputAudioData/womanEng.wav'):
        audiofile = open(audio_file_path, 'rb')
        # transcript = openai.Audio.translate("whisper-1", audiofile)
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audiofile,
            response_format="text"
        )
        print(transcript)

        result = json.loads(str(transcript))['text']
        return result


if __name__ == '__main__':
    whisper_stt = OpenAIstt()
    answer = whisper_stt.run_stt()
    print(answer)
