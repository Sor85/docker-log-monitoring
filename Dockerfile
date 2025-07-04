FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]