#!/bin/bash

# First, generate a Certificate Authority (CA).
openssl genrsa -out root-ca-key.pem 2048
openssl req -x509 -new -nodes -key root-ca-key.pem -subj "/CN=localhost" -sha256 -days 365 -out root-ca.pem

openssl genrsa -out intermediate-key.pem 2048
# echo 'subjectAltName=IP:127.0.0.1' > intermediate.ext
openssl req -new -key intermediate-key.pem -subj "/CN=localhost" -out intermediate.csr
openssl x509 -req -in intermediate.csr -CA root-ca.pem -CAkey root-ca-key.pem -CAcreateserial -out intermediate-ca.key -days 364 -sha256 # -extfile intermediate.ext

