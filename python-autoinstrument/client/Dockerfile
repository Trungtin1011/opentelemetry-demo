# Base image
FROM python:alpine3.20

# Running every next command wih this user
USER root

# Creating work directory in docker
WORKDIR /usr/app

# Copying files to docker
ADD . '/usr/app'

# Installing Flask App
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install opentelemetry bootstrap
RUN opentelemetry-bootstrap -a install

ENV SERVER_ENDPOINT="http://localhost:5555/server_request"
ENV OTEL_SERVICE_NAME="flask-client"
ENV OTEL_RESOURCE_ATTRIBUTES="container.name=flask-client,service.name=flask-client"
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://opentelemetry-collector:4318"
ENV OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"

EXPOSE 8082

# Starting application
ENTRYPOINT ["opentelemetry-instrument", "python", "client.py"]
