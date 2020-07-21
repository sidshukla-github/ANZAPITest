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

# Application Deployment

## Docker component
The application has been containerised using Dockerfile. 
* The dockerfile starts from base python:3 image. 
* It copies relevant file onto the container.
* It installs relevant packages such as flask & requests
* Defines entrypoint for the main application to run

## Google cloud build for CI

Google cloud build has been utilized to build a CI pipeline. The cloud build CI pipeline defines a trigger which kicks in when the code is commited to this gitrepo. It has been configured to look for changes in main code and/or Dockfile. If there is any changes to any of these files, the CI pipeline kicks in.

The coud build configuration is defined using cloubuil.yml file. This configuration file does the following:

* Builds the image using Dockerfile
* Tags the image using appinfo:SHA ( the first seven characters of COMMIT_SHA)
* Runs the container image and executes unit test defined in AppUT.py. The unit testing file is not comprehensive in its scope. The idea is just to demonstrate one of the approaches of executing unit testing. In reality you could use something like 'unittest' package which is more sophisticated. If the unit test fails, the CI pipeline fails!
* On successful execution of unit test case, the image gets stored in GCP container registry









