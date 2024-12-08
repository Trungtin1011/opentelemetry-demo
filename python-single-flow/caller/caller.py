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

@app.route("/server_request")
def server_request():
    python_caller = ""
    param = request.args.get("param")

    logger.info(f"Python Single Caller: Received request {param} from Python Single Client!")

    logger.info(f"Python Single Caller: Attempting to connect Python Server at {STATIC_ENDPOINT}")
    try:
        response_py = requests.get(STATIC_ENDPOINT, headers={})
        response_py.raise_for_status()

        logger.info("Python Single Caller: Reached Python Single Server.")
        python_caller += "Python Single Caller: Reached Python Single Server."

    except requests.exceptions.RequestException as e_py:
      logger.error(f"Python Single Caller Failed: {e_py}")
      python_caller += f"Python Single Caller Failed: {e_py}"

    return python_caller

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port=5555)
