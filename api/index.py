from flask import Flask

app = Flask(__name__)

jwks_file = open("jwks.json", "r")
jwks_contents = jwks_file.read()
jwks_file.close()

response_file = open("response.txt", "r")
response_contents = response_file.read()
response_file.close()

@app.route("/<user_id>/.well-known/jwks.json")
def jwks(user_id):
    resp = app.Response()
    resp.set_data(value=response_contents)
    return resp