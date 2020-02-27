import os

from flask import Flask, request, jsonify
import uwsgidecorators

from detector import Detector


app = Flask(__name__)

HUB_MODEL_URL = os.environ['HUB_MODEL_URL']


@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'OK'}), 200

 
@app.route('/detect', methods=['POST'])
def detect():
    global detector
    if 'file' in request.files:
        image_bin = request.files['file'].stream.read()
        result = detector.detect(image_bin)
        return jsonify({'result': result}), 200
    else:
        return jsonify({'message': 'Unprocessible Entity'}), 422


@uwsgidecorators.postfork
def prepare():
    global detector
    detector = Detector(HUB_MODEL_URL)
    detector.prepare()
