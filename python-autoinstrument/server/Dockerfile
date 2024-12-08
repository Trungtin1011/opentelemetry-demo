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

ENV OTEL_SERVICE_NAME="flask-server"
ENV OTEL_RESOURCE_ATTRIBUTES="container.name=flask-server,service.name=flask-server"
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://opentelemetry-collector:4318"
ENV OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"

# Exposing the flask app port from container to host
EXPOSE 5555

# Starting application
ENTRYPOINT ["opentelemetry-instrument", "python", "server.py"]
