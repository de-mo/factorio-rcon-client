FROM python:latest

ENV HOSTNAME=127.0.0.1
ENV PORT=27015

RUN pip3 install factorio-rcon-py

WORKDIR /usr/src/app

COPY ./rcon_client.py .
COPY ./make_admin.py .

CMD python rcon_client.py $HOSTNAME $PORT
