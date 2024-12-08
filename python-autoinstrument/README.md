# Python auto-instrumentation demo

Flask-server app that listen to port `5555/TCP` with the default endpoint is: `0.0.0.0:5555/server_request`

<br>

Flask web client that has a button for sending requests to **Flask Server**. The web application get server endpoint through an environment variable named `SERVER_ENDPOINT` that point to the server endpoint in the form of: `http://server_ip:5555/server_request`

<br>

To build image for the 2 applications use **docker compose** (v2) and run: `docker compose build`

<br>

Both applications are pre-installed with OpenTelemetry Zero-Code libraries, to configure the applications to send telemetry to OpenTelemetry Collector, configure some additional environment variables:

<br>

```json
server = {
  environment = [
    { name = "OTEL_SERVICE_NAME", value = "flask-server" },
    { name = "OTEL_RESOURCE_ATTRIBUTES", value = "container.name=flask,service.name=flask-server,service.version=1.0.0" },
    { name = "OTEL_EXPORTER_OTLP_ENDPOINT", value = "http://otel-collector:4318" },
    { name = "OTEL_EXPORTER_OTLP_PROTOCOL", value = "http/protobuf" },
    { name = "OTEL_TRACES_EXPORTER", value = "otlp" },
    { name = "OTEL_METRICS_EXPORTER", value = "none" },
    { name = "OTEL_LOGS_EXPORTER", value = "none" },
  ]
}
```

<br>

```json
client = {
  environment = [
    { name = "SERVER_ENDPOINT", value = "http://flask-server:5000/server_request" },
    { name = "OTEL_SERVICE_NAME", value = "flask-client" },
    { name = "OTEL_RESOURCE_ATTRIBUTES", value = "container.name=client,service.name=flask-client,service.version=1.0.0" },
    { name = "OTEL_EXPORTER_OTLP_ENDPOINT", value = "http://otel-collector:4318" },
    { name = "OTEL_EXPORTER_OTLP_PROTOCOL", value = "http/protobuf" },
    { name = "OTEL_TRACES_EXPORTER", value = "otlp" },
    { name = "OTEL_METRICS_EXPORTER", value = "none" },
    { name = "OTEL_LOGS_EXPORTER", value = "none" },
  ]
}
```
