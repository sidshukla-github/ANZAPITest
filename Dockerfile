# Get base image from python
FROM python:3 

# add main file AppInfo.py in this case to the container

#ADD AppInfo.py /

ADD ./* /

# install flask

RUN pip install flask

RUN pip install requests

RUN chmod +x AppInfo.py

RUN chmod +x AppUT.py

#CMD [ "AppInfo.py" ]

ENTRYPOINT ["python", "AppInfo.py"]

