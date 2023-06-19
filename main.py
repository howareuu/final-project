from flask import Flask
from random import choices

app = Flask(__name__)


def random_fruit():
    """Returns random fruit"""
    fruits = ["apple", "cherry", "orange"]
    return choices(fruits)


@app.route("/")
def fruit():
    """Return random fruit"""
    my_fruit = random_fruit()
    return {"messgae": "Hello CD project-new deploy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)