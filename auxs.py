import re
from dateparser import parse
from datetime import datetime, timedelta

def normalizar_expresion(texto):
    texto = texto.lower()
    if re.search(r'la semana que viene', texto):
        return "en 7 días"
    if re.search(r'el mes que viene|la próxima semana', texto):
        return "en 30 días"
    # Agregar otras transformaciones si hace falta
    return texto

expresion = "la semana que viene"
texto_normalizado = normalizar_expresion(expresion)
fecha = parse(texto_normalizado, languages=["es"], settings={"RELATIVE_BASE": datetime.now()})

print(fecha)
