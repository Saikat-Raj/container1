import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get container2 service URL from environment variable
CONTAINER2_URL = os.getenv("CONTAINER2_URL", "http://container2-service:6001")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    file = data.get("file")
    product = data.get("product")

    if not file:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    if not os.path.exists(os.path.join("/data", file)):
        return jsonify({"file": file, "error": "File not found."}), 404

    response = requests.post(
        f"{CONTAINER2_URL}/calculate", json={"file": file, "product": product}
    )
    return response.json(), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
