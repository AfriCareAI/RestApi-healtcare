from fastapi import FastAPI, Query,Form, UploadFile
from typing import Annotated
from pymongo import mongo_client
import requests
import json
import fitz
from PyPDF2 import PdfReader


# setup authentification
app = FastAPI()


@app.get('/')
async def root():
    return {"message":"hello world"}

@app.post('/login/')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

@app.post('/register/')
async def register(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {
        "username": username,
        "password": password
    }

@app.post('/chat/')
async def chat(text: Annotated[str, Form()]):
    base_url = "https://api.openai.com/v1/"
    openai_token = ""
    
    openai_header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(openai_token)
    }

    data = {
        "model": "gpt-3.5-turbo", # model choose
        "messages": [
            {
                "role": "user",
                "content": "J'ai actuellement des donnees medicales d'un individu et j'aimerais que tu m'ecrive un rapport de ce patient avec ces caracteristiques:"+text
            }
        ]
    }

    response = requests.post(base_url+"/chat/completions", headers=openai_header, json=data)
    response  = json.loads(response.text)
    return response['choices'][0]['message']['content']

@app.post('/document/')
async def document(file: UploadFile):
    reader = PdfReader(file.file)
    
    return {
        "filename": file.filename,
        "text": text
    }
