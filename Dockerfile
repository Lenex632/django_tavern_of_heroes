FROM python:3.11

RUN apt-get update

WORKDIR /usr/src/app
COPY requirements.txt .
COPY myapp .
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
