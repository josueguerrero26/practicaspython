from autocorrect import Speller

corrector = Speller(lang='es')

def corregir_texto(texto):
    """Corrige errores ortográficos en el texto dado."""
    if not  corrector(texto) == texto:
         return "Texto corregido:", corrector(texto)
    else:
        print("No se encontraron errores ortográficos.")

print(corregir_texto("me guzta el egercisio"))