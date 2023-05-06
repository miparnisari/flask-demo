## demo

To generate private and public keys

```shell
openssl genrsa -out jwtRSA256-private.pem 2048

openssl rsa -in jwtRSA256-private.pem -pubout -outform PEM -out jwtRSA256-public.pem
```

and then to create a signed JWT


```shell
echo -n '{"alg":"RS256","typ":"JWT", "issuer":"http://35.92.85.155/logout?redirect=https://flask-demo-alpha.vercel.app"}' | base64 | sed s/\+/-/ | sed -E s/=+$//

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsICJpc3N1ZXIiOiJodHRwOi8vMzUuOTIuODUuMTU1L2xvZ291dD9yZWRpcmVjdD1odHRwczovL2ZsYXNrLWRlbW8tYWxwaGEudmVyY2VsLmFwcCJ9

echo -n '{"user":"admin"}' | base64 | sed s/\+/-/ | sed -E s/=+$//

eyJ1c2VyIjoiYWRtaW4ifQ

echo -n "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsICJpc3N1ZXIiOiJodHRwOi8vMzUuOTIuODUuMTU1L2xvZ291dD9yZWRpcmVjdD1odHRwczovL2ZsYXNrLWRlbW8tYWxwaGEudmVyY2VsLmFwcCJ9.eyJ1c2VyIjoiYWRtaW4ifQ" | openssl dgst -sha256 -binary -sign jwtRSA256-private.pem  | openssl enc -base64 | tr -d '\n=' | tr -- '+/' '-_'

SECRET!
```