import os
from typing import List
from threading import Lock

from fastapi import FastAPI, File
from pydantic import BaseModel

from detector import Detector


HUB_MODEL_URL = os.environ['HUB_MODEL_URL']

app = FastAPI(
    title="Off-the-shelf Object Detector",
    description="Off-the-shelf Object Detection API with a model in Tensorflow Hub",
    version="0.0.0",
)
lock = Lock()


class RootOut(BaseModel):
    message: str


class DetectOut(BaseModel):
    message: str
    result: List[List[float]]


@app.get('/', response_model=RootOut)
def root():
    return RootOut(message='OK')

 
@app.post('/detect', response_model=DetectOut)
def detect(file: bytes = File(...)):
    global detector, lock
    with lock:
        result = detector.detect(file)
    return DetectOut(message='OK', result= result)


def prepare():
    global detector, lock
    with lock:
        detector = Detector(HUB_MODEL_URL)
        detector.prepare()


prepare()
