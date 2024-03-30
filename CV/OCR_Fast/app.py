
import uvicorn
from fastapi import FastAPI, Form, Body, Request

from fastapi import FastAPI
from pydantic import BaseModel

from . import AZ


class Items(BaseModel):
    url1: str |None
    url2: str |None
    url3: str |None 

app = FastAPI()

@app.get('/')
async def index():
    return {'Hello' : 'Abhay'}
       
    return req_info


@app.post('/url')
def url(data: dict):
    values = data
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_image_from_url(j)
        ls[i] = result
    return ls
    
    

@app.post('/local')
def local(data: Items):
    
    values = dict(data)
    #print(values)
        
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_image_local(j)
        ls[i] = result
    return ls


if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= 4000)
 

#uvicorn app:app --reload