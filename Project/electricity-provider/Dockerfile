FROM --platform=$BUILDPLATFORM python:3.12.0-alpine3.17 AS builder
EXPOSE 8000
EXPOSE 5432
WORKDIR /app 
COPY requirements.txt /app
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev --no-cache
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
COPY init.sh /app/init.sh
RUN chmod +x /app/init.sh
ENTRYPOINT ["sh", "/app/init.sh"] 



