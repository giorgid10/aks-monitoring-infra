from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/")
def index():
    return jsonify(
        message="AKS monitoring demo",
        host=socket.gethostname()
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)