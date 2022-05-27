
import requests
import os

def hello_http(request):
    print("Calling API")
    print("Env: " + os.environ["bye_url"])
    r = requests.get(os.environ["bye_url"])
    return "Hello " + r.text