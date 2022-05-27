
import importlib
from flask import escape
import functions_framework

from functions.hello import *
from functions.bye import *


@functions_framework.http
def hello(request):
    return hello_http2(request)

def bye(request):
    return bye_http(request)