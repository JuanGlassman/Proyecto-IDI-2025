import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_dep_news_trf") 

def detectar_tiempo_verbal(texto: str):
    """
    Detecta tiempos verbales en español usando spaCy.
    """
    doc = nlp(texto)
    resultados = []

    
    for token in doc:
        # Verbos simples en pasado
        if token.pos_ in {"VERB", "AUX"} and token.morph.get("Tense") == ["Past"]:
            resultados.append((token.text, "Pasado simple/Imperfecto"))

    # Perfecto compuesto y pluscuamperfecto
    for i in range(len(doc)-1):
        if doc[i].lemma_ == "haber" and doc[i].pos_ == "AUX":
            if doc[i+1].morph.get("VerbForm") == ["Part"]:
                if doc[i].morph.get("Tense") == ["Pres"]:
                    resultados.append((f"{doc[i].text} {doc[i+1].text}", "Pretérito perfecto compuesto"))
                elif doc[i].morph.get("Tense") == ["Past"]:
                    resultados.append((f"{doc[i].text} {doc[i+1].text}", "Pretérito pluscuamperfecto"))
    
    if not resultados: 
        for token in doc:
            # Futuro simple
            if token.pos_ in {"VERB", "AUX"} and token.morph.get("Tense") == ["Fut"]:
                resultados.append((token.text, "Futuro simple"))

        # Futuro compuesto
        for i in range(len(doc)-1):
            if doc[i].lemma_ == "haber" and doc[i].pos_ == "AUX" and doc[i].morph.get("Tense") == ["Fut"]:
                if doc[i+1].morph.get("VerbForm") == ["Part"]:
                    resultados.append((f"{doc[i].text} {doc[i+1].text}", "Futuro compuesto"))

        # Futuro perifrástico: ir + a + infinitivo
        for i in range(len(doc)-2):
            if doc[i].lemma_ == "ir" and doc[i].morph.get("Tense") == ["Pres"]:
                if doc[i+1].text.lower() == "a" and doc[i+2].morph.get("VerbForm") == ["Inf"]:
                    resultados.append((f"{doc[i].text} {doc[i+1].text} {doc[i+2].text}", "Futuro perifrástico"))

    if not resultados: 
        for token in doc:
            # Presente simple
            if token.pos_ == "VERB" and token.morph.get("Tense") == ["Pres"]:
                resultados.append((token.text, "Presente"))

        # Presente progresivo: estar + gerundio
        for i in range(len(doc)-1):
            if doc[i].lemma_ == "estar" and doc[i].morph.get("Tense") == ["Pres"]:
                if doc[i+1].morph.get("VerbForm") == ["Ger"]:
                    resultados.append((f"{doc[i].text} {doc[i+1].text}", "Presente progresivo"))

    return resultados if resultados else f"No se detectó tiempo para la oración"


