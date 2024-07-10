from gtts import gTTS
from datetime import datetime
import os
from playsound import playsound
import time


class GoogleGtts:

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

        start = time.time()
        tts = gTTS(tts_text, lang='ko', slow=False)
        end = time.time()
        print(f'gtts tts end {end - start:.3f}sec\n')
        file_name = self.audio_file_name()
        loc = './data/outputAudioData' + file_name
        tts.save(loc)

        gtts_tts = end - start

        start = time.time()
        playsound(loc)
        end = time.time()
        print(f'gtts play end {end - start:.3f}sec\n')

        gtts_play = end - start
        return gtts_tts, gtts_play


if __name__ == '__main__':
    gtts_tts = GoogleGtts()
    gtts_tts.create_output_folder('../Data/outputAudioData')
    gtts_tts.run_tts(text="안녕하세요")
