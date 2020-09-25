# coding: utf-8
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

from app.utils import *

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['Secret'] = "Secret"


# To prevent Cors issues
@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def index():
    return render_template("index.html");   


# To prevent Cors issues
@app.route('/publish', methods=['POST'])
@cross_origin(supports_credentials=True)
def publish():
    file_path = request.form.get('file_path')
    stream_link = request.form.get('stream_link')
    stream_key = request.form.get('stream_key')
    code = 200

    if file_path is not None and stream_link is not None and stream_key is not None:
        result = ffmpeg_publish(file_path, stream_link, stream_key)
        response = jsonify(result)
        code = result["code"]
    else:
        code = 400
        response = jsonify({
            "status": "error",
            "message": "Please provide all required parameters"
        })
        
    return response, code

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=4321)
