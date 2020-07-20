import requests
import json
import os
import sys
import flask 
from flask import request, jsonify


urlid = 'https://api.github.com/repos/sidshukla-github/ANZAPITest/commits'

tagurlid = "https://api.github.com/repos/sidshukla-github/ANZAPITest/tags"



#if len(sys.argv) == 1:
 #   authtoken = os.environ.get('AUTH_TOKEN')
#else:
 #   authtoken = sys.argv[1] + sys.argv[2]

#print ("authtoke ", authtoken)

headers = {
 #   "Authorization" : authtoken,
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
