import requests
import json
import flask 
from flask import request, jsonify

appdetail = {
    "myapplication": [
{
"version": "1.0",
"lastcommitsha": "abc57858585",
"description" : "pre-interview technical test"
}
]
}

urlid = 'https://api.github.com/repos/sidshukla-github/ANZAPITest/commits'

headers = {
    "Authorization" : "Token dc81e6fca81357528b4fc1e4f6c3b32473869021",
      "Content-Type": "application/json",
      "User-Agent" : "sidshukla-github"  
    }

def invokegithubapi():
    
    response = requests.request("GET", urlid, headers=headers)

    responsejson = response.json()[0]['sha']
    print ("my response is ", responsejson)
    appdetail = {
    "myapplication": [
        {
            "version": "1.0",
            "lastcommitsha": responsejson,
            "description" : "pre-interview technical test"
        }
        ]
        }
    return appdetail
    #return jsonify(response.content)

app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/', methods=['GET'])
def home():
    #return invokegithubapi()
    #return jsonify(appdetail)
    return "Hello, you are on the home page"


@app.route('/api/v1/version', methods=['GET'])
def api_all():
    return invokegithubapi()


app.run()
