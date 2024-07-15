import wave
import datetime
import os

# import winsound
# import pyaudio


class Recording:
    def __init__(self):
        # record config
        self.chunk = 1024  # 녹음 사이즈
        self.format = pyaudio.paInt16  # 음질
        self.channels = 1  # 채널 개수
        self.rate = 16000  # 샘플링 레이트
        self.no_sound_timeout = 5  # 소리가 없는 경우 종료할 시간 (초)

    def recording_speech(self):
        print("Recording Start ...")
        # self.beepsound()

        audio = pyaudio.PyAudio()

        stream = audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )

        frames = []

        last_sound_time = datetime.datetime.now()

        while True:
            data = stream.read(self.chunk * 100)
            frames.append(data)

            if any(abs(x) > 500 for x in data):
                last_sound_time = datetime.datetime.now()

            if (
                datetime.datetime.now() - last_sound_time
            ).total_seconds() > self.no_sound_timeout:
                break
        #  끊을 수 있는지 확인 신호오면 (Check)
        # self.beepsound()

        stream.stop_stream()
        stream.close()
        audio.terminate()

        directory = "../data/recordingData/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = (
            directory + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
        )
        wf = wave.open(filename, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b"".join(frames))
        wf.close()

        print("Recording done ...")
        return filename

    def beepsound(self):
        fr = 500
        du = 700
        winsound.Beep(fr, du)


if __name__ == "__main__":
    record = Recording()
    record.recording_speech()
