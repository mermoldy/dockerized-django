FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/django
WORKDIR /opt/django
ADD . /opt/django
RUN pip install -U pip && pip install -r requirements.txt
