from datetime import datetime

import os
from openai import OpenAI
import json
import time
from playsound import playsound


class OpenAItts:
    def __init__(self):
        # config
        self.client = OpenAI()
        self.OpenAI_key = ''
        self.OpenAI_Organization = ''

        self.client.api_key = self.OpenAI_key
        self.client.api_key = self.OpenAI_Organization

    def audio_file_name(self):
        now = datetime.now()
        file_name = now.strftime('%y%m%d_%H%M%S.mp3')
        return file_name

    def create_output_folder(self, dir):
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
        except OSError:
            print('Fail: Creating directory ' + dir)

    def run_tts(self, tts_text='test'):
        self.create_output_folder('./data/outputAudioData/')

        file_name = self.audio_file_name()
        loc = './data/outputAudioData' + file_name
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=tts_text
        )
        response.stream_to_file(loc)
        playsound(loc)


if __name__ == '__main__':
    tts = OpenAItts()
    tts.create_output_folder('../data/outputAudioData')
    tts.run_tts(text="안녕하세요")
