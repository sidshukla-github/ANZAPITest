FROM python:3 

ADD AppInfo.py /

RUN pip install flask

RUN pip install requests

CMD [ "python", "./AppInfo.py" ]