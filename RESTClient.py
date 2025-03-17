from flask import Flask, request, jsonify
from langdetect import detect, DetectorFactory
from iso_639 import languages

# für Konsistente Detection

app = Flask(__name__)

@app.route('/lg', methods=['GET'])
def detect_language():