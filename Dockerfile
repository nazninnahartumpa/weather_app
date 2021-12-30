FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN apt update
RUN apt install gettext -y

RUN pip uninstall django
RUN pip install -r requirements.txt

