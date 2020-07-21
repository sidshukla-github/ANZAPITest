# Application Information

The application has been built using Python3.The file AppInfo.py is the main program that looks for '/api/v1/version' endpoint invocation.

It returns the following JSON object in response. 

"myapplication": [
        {
            "version": [version of the application],
            "lastcommitsha": [SHA of the last commit],
            "description" : "pre-interview technical test"
        }
        ]
        }
    
It makes the following API calls:

* API call to get the version that was tagged at the time of commit
* API call to get the last commit SHA.





