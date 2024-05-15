from flask import Flask

app = Flask(__name__)


@app.route("/test")
def test():
    return "I am the very model of a modern Roman emperor"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
