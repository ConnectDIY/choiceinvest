FROM python:3.7

WORKDIR /app

COPY requirement.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


COPY ./app ./app

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
