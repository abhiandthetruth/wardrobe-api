FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app
COPY ./.env /code/.env

CMD ["uvicorn", "--app-dir", "app/", "--port", "8000", "--host", "0.0.0.0", "main:app"]
