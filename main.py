
from flask import escape
import functions_framework

from functions.hello import *
from functions.bye import *

from dotenv import load_dotenv

load_dotenv()


@functions_framework.http
def hello(request):
    return hello_http(request)

def bye(request):
    return bye_http(request)