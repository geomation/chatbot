#moudules needed
import pyttsx3
import time
import json
import argparse
import requests
import pydub
import speech_recognition as sr


#get messages form the discord channel
def get_discord_messages(channel_id):
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages',headers= Discord.Headers)
    
    jsonn = json.loads(r.text)

    current_chat = jsonn[0]['content']
    return current_chat

#get chat messages from twitch
def read_twitch_chat():
    pass

#get chat messages from youtube
def read_youtube_chat():
    pass

#records audio data
def get_audio_input():
    r = sr.Recognizer
    with sr.Microphone() as source:
        audio_data = r.record(source , duration=5)

        print("listening....")

        text = r.recognize_sphinx(audio_data)
    
    print(text)
    return text

#AI this bitch
def gernerate_response():
    TTS_control("look, leave me alone,i have no brain because a certain someone is too lazy to code up a neural network")
    pass

#initailise the default tts
def Init_TTS():
    global engine
    voice_input = ""
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)

#pyttsx3 text to speech
def pyttsx3_TTS(message):
    engine.say(message)
    engine.runAndWait()

#dertermine the text to speech service in use
def TTS_control(message):
    if tts_type == "pyttsx3":
        pyttsx3_TTS(message)
    if tts_type == "EL":
        pass

#initailising the programs variables and dependencies
def Init_var():
    global Discord
    global tts_type
    global mode

    #Load Configuration data
    try:
        with open('config.json') as D:
            data =  json.load(D)
    except:
        print('Failed to load file. Please check if it is in the directory.')
        exit()

    class Discord:
        Channel_id = data["Discord"][0]["Channel_id"]
        Headers = data["Discord"][0]["headers"]

    tts_list = ["pyttsx3", "EL"]
    mode_list = ["Discord","Youtube","Twitch","VoiceChat"]

    parser = argparse.ArgumentParser()
    parser.add_argument('-mode','--chat_mode', default='VoiceChat', choices=mode_list, type=str)
    parser.add_argument('-tts','--tts_type', default='pyttsx3', choices=tts_list, type=str)

    args = parser.parse_args()

    tts_type = args.tts_type
    mode = args.chat_mode

    if tts_type == "pyttsx3":
        Init_TTS()

#program loop
if __name__ == "__main__":
    Init_var()
    print("\n\Running!\n\n")

    #TTS_control("There is currently no A I Model installed so all input will be mirrored as output.")


    if mode == "Discord":
        while True:
            get_discord_messages(Discord.Channel_id)
            print("\n\nReset!\n\n")
            time.sleep(2)
            
    if mode == "Twitch":
        TTS_control("No current Twitch support")
        #while True:
            #retrieve_messages(Discord.Channel_id)
            #print("\n\nReset!\n\n")
            #time.sleep(2)

    if mode == "Youtube":
        TTS_control("No current Youtube support")
        #while True:
            #retrieve_messages(Discord.Channel_id)
            #print("\n\nReset!\n\n")
            #time.sleep(2)

    if mode == "VoiceChat":
        while True:
            text = get_audio_input()
            TTS_control(text)
            print("\n\nReset!\n\n")
            time.sleep(2)
