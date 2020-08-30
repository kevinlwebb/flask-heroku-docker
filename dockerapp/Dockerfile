FROM python:3.8.1-slim-buster

COPY . /dockerapp
WORKDIR /dockerapp

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT 5000

CMD gunicorn start:app --bind 0.0.0.0:$PORT