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
    xml = '''
<html>
foo
</html>
HTP/1.1 200 OK
Content-Type: application/json
Content-Length: 443
{ "keys": [ { "alg": "RS256", "x5c": [ "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7uppzfcQ7XRHsbh7W1jPwO6EzJm6FJw69kINSaMBtyQ6RK/Ev+5zRpuZWh0uIOTan4LLz5xnVOMSKSFnZozK/ShYBG/YRY7WApZfdEwB0vW9vbnqZqu+ats1qtxfZOmvjht8EkFwFsHuBr7qfufaRbCW0w8KGxMosjEte8X+9T44JUkPcU9sRhM6dby7ROSwF1ktY1+I7ZAFkfFYcFItXebp2pldD8JxOAqIhrxzEDjxt/P0+F1/B61+uP7EAZSikywRnwNsP4KskgxuogJQmmmPUGns+pg+nNexqxnSiFH1peKQ5A/kyiilaxZPiGqiC6zAibUBeYmz9x9zyymu2wIDAQAB" ] } ] }
'''
    resp = app.make_response(xml)
    resp.content_length = 22
    resp.status_code = 200
    return resp