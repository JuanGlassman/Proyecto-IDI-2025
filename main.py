from builtins import str
from fastapi import FastAPI 
import spacy


app = FastAPI()

nlp_en = spacy.load("en_core_web_sm")
nlp_es = spacy.load("es_core_web_sm")

@app.get("/invertir_texto/") 
def invertir_texto(texto: str): 
    texto_invertido = texto[::-1] 
    return {"respuesta": texto_invertido}

@app.get("/adverbs/") 
def adverbs(texto: str): 
    doc = nlp_es(texto)
    adverbios = [token.text for token in doc if token.pos_ == "ADV"]

    if adverbios:
        return {"respuesta": f"Posee adverbios: {', '.join(adverbios)}"}
    else:
        return {"respuesta": "No posee adverbios"}