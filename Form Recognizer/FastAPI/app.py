
import uvicorn
from fastapi import FastAPI, Form, Body, Request

from fastapi import FastAPI
from pydantic import BaseModel

import AZ


class Items(BaseModel):
    url1: str | None
    url2: str | None
    url3: str | None 

app = FastAPI()


@app.post('/url')
def url(data: Items):
    
    values =  data.dict()
    
    #values = data['urlx']    
    #
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_document_from_url(j) 
        
        ls[i] = result
    return ls

@app.post('/local')
def local(data: Items):
    
    values = data.dict()
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_document_local(j) 
        
        ls[i] = result
    return ls


if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= 8000)
 
#uvicorn app:app --reload