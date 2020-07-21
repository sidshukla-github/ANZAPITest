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
* Runs the container image and executes unit test defined in AppUT.py. The unit testing file is not comprehensive in its scope. The idea is just to demonstrate one of the approaches of executing unit testing. In reality you could use something like 'unittest' package which is more comprehensive and sophisticated. If the unit test fails, the CI pipeline fails!
* On successful execution of unit test case, the image gets stored in GCP container registry

## Versioning

### Application versioning

The application can be versioned using annotated git tags when committing to repo. You could follow a Major-Minor-Patch version tag for your commits. 

### Image versioning 

In this example, I am using $SHORT_SHA (the first seven characters of COMMIT_SHA) to tag the images. This makes the tags unique and is likely the recommended approach for deployments especially in an environment that could scale on multiple nodes. You likely want deliberate deployments of a consistent version of components. If your container restarts or an orchestrator scales out more instances, your hosts won’t accidentally pull a newer version, inconsistent with the other nodes

ALternative to $SHORT_SHA could be to use $BUILD_ID as a tag. Advantage is that it allows you to correlate back to the specific build to find all the artifacts and logs.

Another option could be use a mix and match approach of using $TAG_NAME (name of your tag at the time of commit) and $SHORT_SHA 

# Considerations/Risks

* Authentication -  Review configuration for access for Cloud Build Service Account
* Certified base image - private repository could be leveraged instead of public repos for pulling images
* Scerets - Use GCP Secret Manager or GCP Cloud Key Management Service to store and retreive secret information
* Vulnerability scanning - 
* Multi stage build -  the docker file in this case is not using multi stage build concepts. Recommendation is to leverage multi stage build approach to minimize image size, leverage caching and speeding up build process
* Avoiding upload of unnecessary files - the .dockerignore and .gitignore files can be extended to include more exclusions
* Binary authorization, policy creation and enforcement to identify vulnerable images









