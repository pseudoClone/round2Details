FROM python:3.14-alpine

WORKDIR /app

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python"]

CMD ["app.py"]