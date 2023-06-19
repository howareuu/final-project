from flask import Flask

app = Flask(__name__)

@app.route("/")
def fruit():
    """Return Hello messgae"""
    return {"messgae": "Hello CD project-new deploy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)