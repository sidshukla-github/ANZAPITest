import requests
import json
import os
import sys
import flask 
from flask import request, jsonify

def startunittest():
    print ("Starting unit test")
    
    urlid = 'https://api.github.com/repos/sidshukla-github/ANZAPITest/commits'


    headers = {
 
      "Content-Type": "application/json",
      "User-Agent" : "sidshukla-github"  
    }

    response = requests.request("GET", urlid, headers=headers)

    print ("response is ", response.status_code)

    if response.status_code == 200:
        sys.exit(0)
    else:
        sys.exit(-1)

    

startunittest()