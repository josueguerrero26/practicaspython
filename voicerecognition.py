import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Escuchando...")
    audio = recognizer.listen(source)
text = recognizer.recognize_google(audio, language="es-ES")
print("Has dicho: {}".format(text))


