import os
from google.cloud import speech

class Googlestt:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "stt-to-gpt-to-tts-9c93e4bf4ea7.json"

    def run_stt(self, audio_file_path="./data/inputAudioData/womanEng.wav"):
        # instantiates a client
        print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

        client = speech.SpeechClient()

        gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
        audio = speech.RecognitionAudio(uri=gcs_uri)

        config = speech.RecognitionConfig(
            encodings=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US"
        )

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))


if __name__ == '__main__':
    google_stt = Googlestt()
    google_stt.run_stt()


