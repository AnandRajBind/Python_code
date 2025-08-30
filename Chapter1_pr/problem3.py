
# problem .
# pip install pyttsx3 ( text to speech conversion library in python)


import pyttsx3
engine=pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()