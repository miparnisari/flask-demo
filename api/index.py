from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    print(request.remote_addr)
    return "hi"