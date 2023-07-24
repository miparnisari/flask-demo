from flask import Flask

app = Flask(__name__)

jwks_file = open("jwks.json", "r")
jwks_contents = jwks_file.read()
jwks_file.close()

@app.route("/<user-id>/.well-known/jwks.json")
def jwks(userId):
    return jwks_contents