# app/app.py
from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time
import datetime
import os

app = Flask(__name__)

REQUEST_COUNT = Counter('drviki_request_count', 'Total number of requests')

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""
    <html>
      <head><title>Dr. ViKi DevOps Pipeline</title></head>
      <body>
        <h1>Hello from Dr. ViKi DevOps Pipeline!</h1>
        <p>Timestamp: {ts}</p>
      </body>
    </html>
    """

@app.route("/healthz")
def health():
    return "OK", 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=8080)
    

