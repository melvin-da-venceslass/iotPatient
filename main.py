import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from pydantic import BaseModel
import os
import mdb_client 

mdb = mdb_client.MDB_reader()
app = FastAPI()

class Patient(BaseModel):
    pid:str

class updatePatient(BaseModel):
    pid:str
    name:str
    address:str
    type:str
    operation:str




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

@app.get("/participants", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('participants.html', context={'request': request})

@app.get("/loader", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('loader.html', context={'request': request})

@app.get("/patientsmgr", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('patient_management.html', context={'request': request})

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('home.html', context={'request': request})

@app.post("/getPatient")
def home(pids:Patient):
    try:
        patient = mdb.get_the_patient(pids.pid)
        if patient:
            patient["status"]="success"
            return patient
        else:
            return {"status":"no-user",}
    except:
        return {"status":"Failed"}

@app.post("/savePatient")
def home(data:updatePatient):
    try:
        patient = mdb.save_the_patient(data)
        if patient:
            return {"status":"success"}
        else:
            return {"status":"Failed"}
    except:
        return {"status":"Failed"}

if __name__=="__main__":
    uvicorn.run("main:app",port=5678, reload=True)

