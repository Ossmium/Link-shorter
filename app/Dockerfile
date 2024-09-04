FROM python:3.11.1

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./req.txt /usr/src/app/
RUN pip install -r req.txt

COPY . /usr/src/app/