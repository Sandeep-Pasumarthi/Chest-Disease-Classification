from src.utils.image import decodeImage
from src.pipeline.prediction import PredictionPipeline

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from pathlib import Path

import os


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__, template_folder="templates")
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = Path("inputImage.jpg")
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def train():
    os.system("dvc repro")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, predictor.filename)
    result = predictor.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    predictor = ClientApp()
    app.run(host='0.0.0.0', port=8080)
