FROM python:3.11.6

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["gunicorn", "self_storage.wsgi:application", "--bind", "0:8000" ]
# CMD sleep infinity