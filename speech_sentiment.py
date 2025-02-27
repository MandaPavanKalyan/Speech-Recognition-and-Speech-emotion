from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#import googletrans
import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init()
recogonizer=sr.Recognizer()

with sr.Microphone() as source:
    print("wait for calibrations")
    recogonizer.adjust_for_ambient_noise(source,1)
    print("start speaking")
    audio=recogonizer.listen(source)
    print("recorded successfully")
    speech=recogonizer.recognize_google(audio)
    speech=speech.lower()
    print(speech)

sentence=[str(speech)]
analyser=SentimentIntensityAnalyzer()
for i in sentence:
    a=analyser.polarity_scores(i)
    print(a)
