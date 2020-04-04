#!/usr/bin/env bash
service nginx start
uwsgi --ini /etc/uwsgi/uwsgi.ini --callable app
