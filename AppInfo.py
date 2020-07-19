import requests
import json
import os
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

tagurlid = "https://api.github.com/repos/sidshukla-github/ANZAPITest/tags"



os.environ['Auth'] = 'Token fa7ba2a68acbab8c3934de29bd70e800d287ad82'

headers = {
    "Authorization" : os.environ['Auth'],
      "Content-Type": "application/json",
      "User-Agent" : "sidshukla-github"  
    }

def invokegithubapi():
    
    response = requests.request("GET", urlid, headers=headers)

    responsesha = response.json()[0]['sha']

    response = requests.request("GET", tagurlid, headers=headers)    

    appversion = response.json()[0]['name']
    #print ("my response is ", responsejson)

    appdetail = {
    "myapplication": [
        {
            "version": appversion,
            "lastcommitsha": responsesha,
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
