from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/add", methods=["POST"])
def add():
    input = request.get_json()
    a = input.get("a")
    b = input.get("b")
    sum = a + b
    return jsonify({"sum": sum, "message": "hello1"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
