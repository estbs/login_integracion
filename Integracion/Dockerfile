FROM alpine:3.17

WORKDIR /app
COPY . /app
RUN apk update && apk add --no-cache py3-pip
RUN pip install -r requirements.txt
#puerto en el que se ejecutará la aplicación
EXPOSE 8080
CMD ["python", "app.py"]
