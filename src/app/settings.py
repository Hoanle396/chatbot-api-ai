from os import getenv

ENV = getenv("PY_ENV", "DEV")

BE_HOST = getenv("BE_HOST", "0.0.0.0")
BE_PORT = int(getenv("BE_PORT", 5000))
