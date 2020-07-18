FROM python:3 

ADD AppInfo.py /

RUN pip install flask

CMD [ "python", "./AppInfo.py" ]