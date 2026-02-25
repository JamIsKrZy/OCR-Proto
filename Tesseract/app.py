from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io
import base64

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/ocr", methods=["POST"])
def ocr():
    data = request.get_json()

    # Accept base64 encoded image
    image_data = base64.b64decode(data["image"])
    image = Image.open(io.BytesIO(image_data))

    lang = data.get("lang", "eng")
    config = data.get("config", "")

    text = pytesseract.image_to_string(image, lang=lang, config=config)
    
    # Optionally return bounding box data too
    detail = data.get("detail", False)
    result = {"text": text.strip()}
    
    if detail:
        boxes = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
        result["boxes"] = boxes

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)