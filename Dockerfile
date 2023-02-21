FROM python:3.10

ADD . /app
WORKDIR /app
RUN pip install -e .
ENTRYPOINT ["gunicorn"]
