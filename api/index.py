from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    print(request)
    return "hi"