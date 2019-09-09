import os

from flask import Flask, render_template, request
import json
from tesseractOcr import tesseractOcr
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['file']

    extracted_text = tesseractOcr(file)
    arry = []
    arry.append({
        'text': ''.join(extracted_text.splitlines())
    })

    return json.dumps(arry)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086)
