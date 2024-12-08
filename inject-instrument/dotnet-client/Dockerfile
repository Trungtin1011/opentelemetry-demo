FROM mcr.microsoft.com/dotnet/sdk:8.0-jammy

WORKDIR /app

COPY . .

ENV SERVICE_ENDPOINT="http://127.0.0.1:5050"

EXPOSE 8888

RUN dotnet publish -c Release -o out

ENTRYPOINT ["/bin/sh", "-c", "./out/Examples.Client --urls http://*:8888"]
