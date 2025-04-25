import speech_recognition as sr
import pyttsx3
import webbrowser

renonocer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        audio = renonocer.listen(source)
    try:
        text = renonocer.recognize_google(audio, language="es-ES")
        print("Has dicho: {}".format(text))
        if "buscar" in text:
            text = text.replace("buscar", "")
            webbrowser.open("https://www.google.com/search?q=" + text)
    except:
        print("No te he entendido")

if __name__ == "__main__":
    talk()
