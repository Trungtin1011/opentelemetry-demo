FROM mcr.microsoft.com/dotnet/sdk:8.0-jammy

WORKDIR /app

COPY . .

ENV DB_CONNECTION="Server=mssql,1433;User=sa;Password=Strongpwd@123;TrustServerCertificate=True;"

EXPOSE 5050

RUN dotnet publish -c Release -o out

ENTRYPOINT ["/bin/sh", "-c", "./out/Examples.Service --urls http://*:5050"]
