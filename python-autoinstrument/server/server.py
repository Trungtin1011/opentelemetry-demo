from flask import Flask, request
import logging

# Disable  * Serving Flask app 'server' AND * Debug mode: off
#cli.show_server_banner = lambda *x: None

logging.getLogger('werkzeug').disabled = True
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/server_request")
def server_request():
    req = request.args.get("param")

    logger.info(f"{req}")

    return "Python Auto-instrument Server: Served!"


if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port=5555)
