import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

def SpeakText(command):
        # Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

while(1):
    try:
        with sr.Microphone() as source:
            print("wait for the calibaration")
            r.adjust_for_ambient_noise(source,1)
            print("start speaking")
            audio=r.listen(source)
            speech=r.recognize_google(audio)
            speech=speech.lower()

            print("did you say "+ speech)
            SpeakText(speech)
            
    except sr.UnknownValueError:
        print("unknown error occured")
