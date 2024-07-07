import os

class Config:
    secret_key = os.urandom(24)
    SECRET_KEY = secret_key
    