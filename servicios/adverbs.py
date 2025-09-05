from builtins import str
import spacy


nlp = spacy.load("es_core_news_sm")

def adverbs(texto: str): 
    doc = nlp(texto)
    adverbios = [token.text for token in doc if token.pos_ == "ADV"]

    if adverbios:
        return {"respuesta": f"Posee adverbios: {', '.join(adverbios)}"}
    else:
        return {"respuesta": "No posee adverbios"}