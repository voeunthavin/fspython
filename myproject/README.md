# Get started

`py -3 -m venv .venv`

## To run hello.py

`flask --app hello run`

## Externally visible server

`flask run --host=0.0.0.0`

## Generate good secret keys

`py -c 'import secrets; print(secrets.token_hex())'`
