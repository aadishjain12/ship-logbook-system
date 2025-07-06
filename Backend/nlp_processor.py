import spacy

nlp = spacy.load("en_core_web_sm")

def process_voice_log(text):
    doc = nlp(text)
    return {
        'speed': next((ent.text for ent in doc.ents if ent.label_ == "CARDINAL"), None),
        'action': text
    }
