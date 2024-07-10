import pyaudio
import wave
import datetime
import winsound

# record config
CHUNK = 1024                # 녹음 사이즈
FORMAT = pyaudio.paInt16    # 음질
CHANNELS = 1                # 채널 개수
RATE = 16000                # 샘플링 레이트
NO_SOUND_TIMEOUT = 5        # 소리가 없는 경우 종료할 시간 (초)

def beepsound():
    fr = 500
    du = 700
    winsound.Beep(fr, du)

def recording():
    print("Recording Start ...")
    beepsound()

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)

    frames = []

    start_time = datetime.datetime.now()

    last_sound_time = datetime.datetime.now()

    while True:
        data = stream.read(CHUNK*100)
        frames.append(data)

        if any(abs(x) > 500 for x in data):
            last_sound_time = datetime.datetime.now()

        if(datetime.datetime.now() - last_sound_time).total_seconds() > NO_SOUND_TIMEOUT:
            break

    beepsound()

    stream.stop_stream()
    stream.close()
    audio.terminate()

    filename = "./data/recordingData/" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Recording done ...")
    return filename

if __name__ == '__main__':
    beepsound()