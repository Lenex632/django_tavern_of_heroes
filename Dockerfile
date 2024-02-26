FROM python:3.11

RUN apt-get update

WORKDIR /usr/src/app
COPY requirements.txt .
COPY myapp .
RUN pip install -r requirements.txt

RUN chmod +x start.sh
CMD ["/bin/sh", "start.sh"]
