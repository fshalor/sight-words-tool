FROM ubuntu:18.04

MAINTAINER fshalor "ken@stacktosea.com"

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx libncurses5-dev libncursesw5-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]
