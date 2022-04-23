import uvicorn
import math
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse,PlainTextResponse
from pydantic import BaseModel
from typing import Optional
from ELA import test_image_with_ela
import numpy as np
import os
app = FastAPI()

origins = [
    "https://localhost", "http://localhost",
    "https://localhost:5050", "http://localhost:5050",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

tmp = str(os.getcwd())+"/static/tempo/"
print(tmp)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})





@app.post("/img2img/")
async def upload_file(file: UploadFile = File(...)):
    image = await file.read()
    # filename = file.filename
    with open(f"{tmp}{file.filename}", "wb") as f:
        f.write(image)
    
    path = f"{tmp}{file.filename}"
    result = test_image_with_ela(path)
    return {"Filename":str(file.filename),"Result":str(result[0]),"Score":round(float(result[1])*100,2),"File":"/static/tempo/"+file.filename}
