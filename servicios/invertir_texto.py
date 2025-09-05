from builtins import str

def invertir_texto(texto: str): 
    texto_invertido = texto[::-1] 
    return {"respuesta": texto_invertido}
