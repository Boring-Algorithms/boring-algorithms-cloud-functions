
import requests
import os

def hello_http(request):
    r = requests.get(os.environ["BYE_URL"])
    return "Hello " + r.text