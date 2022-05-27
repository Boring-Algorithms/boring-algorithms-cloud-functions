
import os

def secret_token_valid(token):
    return token == os.environ["SECRET_KEY"]