from textblob import TextBlob    
import traductor as tr

def analizar_sentimiento(text):
    blob = TextBlob(text)
    
    polaridad = blob.sentiment.polarity
    subjetividad = blob.sentiment.subjectivity
    etiquetas = blob.tags

    if polaridad > 0:
        sentimiento = 'positivo'
    elif polaridad < 0:
        sentimiento = 'negativo'
    print ("Analisis de sentimiento")
    print("-------------------------------")
    print ("Todo texto se traduce al ingles para analizarlo")
    print(f'{text}')
    print(f'polaridad: {polaridad}')
    print(f'subjetividad: {subjetividad}')
    print(f'sentimiento: {sentimiento}')
    print(f'etiquetas: {etiquetas}')


txt = input("Como te sientes el dia de hoy:  ")
txt_traducido = tr.traduc(txt)
analizar_sentimiento(txt_traducido)
# Compare this snippet from A_PROYECTOS/sentimiento.py: