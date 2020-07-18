import flask 
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

appdetail = {
    "myapplication": [
{
"version": "1.0",
"lastcommitsha": "abc57858585",
"description" : "pre-interview technical test"
}
]
}


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/appinfo', methods=['GET'])
def api_all():
    return jsonify(appdetail)


app.run()