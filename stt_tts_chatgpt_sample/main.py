import time

from STT.stt_ETRI import ETRIstt
from STT.stt_openai import OpenAIstt
from STT.stt_google import Googlestt

from TTS.tts_gtts import GoogleGtts

from gpt.chatGPT import ChatGPTapi

from audioRecord import wav_recording as record
import argparse

def args_parser():
    '''
    STT : ETRI, GOOGLE, OPENAI(ONLY ENG)
    TTS : GTTS
    GPT: GPT3, INSTRUCT-GPT, ChatGPT
    Translation option ; Y, N
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("--stt", "-s", dest="stt_use", default="etri",
                        choices=['etri', 'google', 'hae', 'openai'], help="STT type, type = String")
    parser.add_argument("--tts", "-t", dest="tts_use", default="hae",
                        choices=['gtts', 'hae'], help="TTS type, type = String")
    parser.add_argument("--gpt", "-g", dest="gpt_use", default="chatgpt",
                        choices=['gpt3', 'instruct', 'chat'], help="GPT type, type = String")
    parser.add_argument("--trans", dest="trans_use", required=False,
                        default="n", help="trans type, type = Boolean")

    return parser.parse_args()

if __name__ == '__main__':
    history = []
    args = args_parser()
    # STT choose .. default - ETRI STT
    if args.stt_use == 'openai':
        stt_use = OpenAIstt()
    elif args.stt_use == 'google':
        stt_use = Googlestt()
    else:
        stt_use = ETRIstt()

    # GPT choose : default - chatgpt
    gpt_use= ChatGPTapi()

    # TTS choose .. default - HAE TTS
    if args.tts_use == 'gtts':
        tts_use = GoogleGtts()


    while True:
        filename = record.recording()
        print('Recording File Dir : ' + filename)

        question = stt_use.run_stt(audio_file_path=filename)
        print('Input Question : ' + question)

        start_time = time.time()
        if args.trans_use != 'n':
            answer, history = gpt_use.do_chat(question=question, history=history)
        else:
            answer, history = gpt_use.do_chat(question=question, history=history)

        end_time = time.time()
        print(end_time)
        print(f'total time : {end_time-start_time:.3f}')

        tts_use.run_tts(tts_text=answer)

        if '종료' in question:
            break

    time.sleep(5)
