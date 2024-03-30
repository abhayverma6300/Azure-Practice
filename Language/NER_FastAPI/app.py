from fastapi import FastAPI, Form
from typing import Dict
from . import AZ

app = FastAPI()

@app.post("/custom_ner_local")
async def recognize_custom_entities_local(document: str = Form(...)) -> Dict:
    values = {"document": document}
    ls = {}
    for i,j  in values.items():
        result = AZ.recognize_custom_entities_local(j)
        ls[i] = result
    return ls
