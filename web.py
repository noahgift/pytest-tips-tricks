from flask import Flask, jsonify
from mlib.mchange import change

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"hello": "bob"})


@app.route("/change/<dollar>/<cents>")
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
