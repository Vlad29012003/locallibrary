FROM python:3.8

LABEL maintainer="vladosmen29@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt && \ apt-get clean && \ rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY  . .

VOLUME [ "/app/static" ]

EXPOSE 8000

ENTRYPOINT [ "python3" , "manage,py" , "runserver" , "0.0.0.0:8000" ]