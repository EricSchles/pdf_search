FROM elasticsearch:7.3.0 as elasticsearch
WORKDIR /app

FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN apt-get install -y python-dev
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN apt-get update -y

COPY ./requirements.txt /myapp/requirements.txt
WORKDIR /myapp
COPY --from=elasticsearch /app /myapp 
RUN python3 -m pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]