FROM python:3.8

LABEL maintainer="vladosmen29@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get upgrade -y
RUN pip install -r requirements.txt

COPY . ./app

VOLUME [ "/app/static" ]

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8001"]
