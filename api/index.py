from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    print(request.args.get('data'))
    return "hi"

@app.route("/post", methods=['POST'])
def index():
    print(request.json)
    return "OK"