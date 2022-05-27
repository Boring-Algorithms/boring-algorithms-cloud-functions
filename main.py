
import collections
from flask import escape
import functions_framework

from functions.hello import *
from functions.bye import *

from dotenv import load_dotenv
load_dotenv()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



@functions_framework.http
def hello(request):
    return hello_http(request)

def bye(request):
    return bye_http(request, db)