# OpenTelemetry Demo Application

**Repo Owner**: Tin Trung Ngo

## Before you begin

This repository contains image build artifacts for a demo application of OpenTelemetry Instrumentation in Kubernetes environment that utilizes [OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator).

For Amazon ECS, it is normally recommended to use AWS Distro for OpenTelemetry (ADOT) collector for container instrumentation. The images in this repository use the original open-source OpenTelemetry Collector instead of ADOT collector.

<br>

## Repository structure
1. Folder [python-autoinstrument](./python-autoinstrument) contains source code to build required images for Python autoinstrumentation application.
2. Folder [inject-instrument](./inject-instrument) contains source code to build a full-flow OpenTelemetry Demo application with multiple components and language

<br>


<br>
