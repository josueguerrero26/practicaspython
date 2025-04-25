from translate import Translator

def traduc(txt):
    
    traductor = Translator(from_lang = "spanish", to_lang ='english')

# txt_traducido = traductor.translate(txt)
    return f"Traducido al ingles: {traductor.translate(txt)}" 

# txt = input("Introduce el texto a traducir: ")
# print(traduc(txt))