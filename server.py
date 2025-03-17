from flask import Flask, request, jsonify
from langdetect import detect, detect_langs, DetectorFactory
from iso639 import languages

# für Konsistente Detection
DetectorFactory.seed = 0

app = Flask(__name__)

@app.route('/lg', methods=['GET'])
def detect_language():
    """
    Überprüft den per HTTP Anfrage übergebenen Text auf Sprache, Accuracy und Verstrauenswürdikeit

    Returns:
        JSON: im JSON format:
            reliable (boolean): reliability
            language (string): found language full name
            short (string): found language short name
            prob (float): probability in percent (xxx.xx)
    """
    text = request.args.get("id")
    if not text:
        return jsonify({"error": "Kein Text angegeben"}), 400

    try:
        lang_code = detect(text)
        lang_prob = detect_langs(text)[0].prob * 100        # Wahrscheinlichkeit finden
        lang_name = languages.get(alpha2=lang_code).name    # Voller Name der Sprache

        reliable = lang_prob > 50                           # wenn > 50 = reliable

        response = {
            "reliable": reliable,
            "language": lang_name.upper(),
            "short": lang_code,
            "prob": round(lang_prob, 2)
        }

        # response in String umwandeln
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)