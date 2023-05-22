FROM continuumio/miniconda3

WORKDIR /home/app

RUN apt-get update -y 
RUN apt-get install nano unzip
RUN apt-get install -y python3.10
RUN apt install curl -y

RUN curl -fsSL https://get.deta.dev/cli.sh | sh

COPY requirements.txt /dependencies/requirements.txt
RUN pip install -r /dependencies/requirements.txt

RUN curl -fsSL https://get.deta.dev/cli.sh | sh
RUN pip install fastapi "uvicorn[standard]" pydantic typing pandas gunicorn openpyxl

COPY . /home/app


CMD gunicorn app:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker --timeout 30

#CMD gunicorn --worker-class uvicorn.workers.UvicornWorker 