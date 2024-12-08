from flask import Flask, jsonify, request, cli
import requests, os
import logging

# Disable  * Serving Flask app 'server' AND * Debug mode: off
#cli.show_server_banner = lambda *x: None

logging.getLogger('werkzeug').disabled = True
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

STATIC_ENDPOINT = os.environ.get('STATIC_ENDPOINT', 'http://localhost:8000/')
NET_ENDPOINT = os.environ.get('NET_ENDPOINT', 'http://localhost:8888/')

@app.route("/server_request")
def server_request():
    python_caller = ""
    dotnet_caller = ""
    param = request.args.get("param")

    logger.info(f"Caller: Received request {param} from Python Client!")

    logger.info(f"Python Caller: Attempting to connect Python Server at {STATIC_ENDPOINT}")
    try:
        response_py = requests.get(STATIC_ENDPOINT, headers={})
        response_py.raise_for_status()

        logger.info("Python Caller: Reached Python Server.")
        python_caller += "Python Caller: Reached Python Server."
        #return response_py.text, response_py.status_code

    except requests.exceptions.RequestException as e_py:
      logger.error(f"Python Caller Failed: {e_py}")
      python_caller += f"Python Caller Failed: {e_py}"

    logger.info(f"Dotnet Caller: Attempting to trigger .NET Client at {NET_ENDPOINT}")
    try:
        response_net = requests.get(NET_ENDPOINT, headers={})
        response_net.raise_for_status()

        if "Dotnet Client Error:" in response_net.text:
            logger.error("Dotnet Caller Failed: .NET Client Error.")
            dotnet_caller += "Dotnet Caller Failed: .NET Client Error."
        else:
            logger.info("Dotnet Caller: Triggered .NET Client.")
            dotnet_caller += "Dotnet Caller: Triggered .NET Client."

    except requests.exceptions.RequestException as e_net:
      logger.error(f"Dotnet Caller Failed: {e_net}")
      dotnet_caller += f"Dotnet Caller Failed: {e_net}"

    return "\n" + python_caller + "\n" + dotnet_caller

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port=5555)
