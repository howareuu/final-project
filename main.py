from flask import Flask, request, jsonify

from predict.mlib import predict

app = Flask(__name__)


@app.route("/")
def fruit():
    """Return Hello message"""
    return {"message": "Welcome to ML project of Continuous Delivery!"}


@app.route("/predict", methods=["POST"])
def predict_height():
    """Predicts the Height of MLB Players"""

    json_payload = request.json
    print(f"JSON payload: {json_payload}")
    prediction = predict(json_payload["Weight"])
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
