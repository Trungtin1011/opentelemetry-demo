from flask import Flask, request, cli
import logging

# Disable  * Serving Flask app 'server' AND * Debug mode: off
#cli.show_server_banner = lambda *x: None

logging.getLogger('werkzeug').disabled = True
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():

  logger.info("Python Server: Reached!")
  return ("Python Server: Reached!")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False, port=8000)
