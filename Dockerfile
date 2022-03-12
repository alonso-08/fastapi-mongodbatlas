FROM python:3.10.2
COPY . /usr/src/app

WORKDIR /usr/src/app


RUN python3 -m pip install -r requirements.txt


CMD [ "uvicorn", "app:app","--host","127.0.0.1","--port","8080" ]
