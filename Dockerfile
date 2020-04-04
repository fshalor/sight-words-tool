FROM ubuntu:18.04

MAINTAINER fshalor "ken@stacktosea.com"

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx libncurses5-dev libncursesw5-dev nginx 

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /srv/app/requirements.txt

WORKDIR /srv/app

RUN pip3 install -r requirements.txt

COPY . /srv/app

# Setup uwsgi and supervisord
COPY server-conf/uwsgi.ini /etc/uwsgi/

COPY server-conf/nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]

#ENTRYPOINT [ "python3" ]

#CMD [ "app/app.py" ]
