## demo

```shell
openssl genrsa -out jwtRSA256-private.pem 2048

openssl rsa -in jwtRSA256-private.pem -pubout -outform PEM -out jwtRSA256-public.pem

```