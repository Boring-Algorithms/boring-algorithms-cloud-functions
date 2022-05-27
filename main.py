
import collections
from flask import escape
import functions_framework

from functions.hello import *
from functions.bye import *
from algorithms.sort_algorithms import *
from algorithms.algorithm_manager import *

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

@functions_framework.http
def bye(request):
    return bye_http(request, db)

@functions_framework.http
def get_alrotithms(request):
    return get_algorithms_dict()

# @functions_framework.http
# def get_alrotithms(request):
#     return get_algorithms_dict()
    # collection = db.collection(u'algorithms')
    # docs = collection.stream()
    # res = []
    # for doc in docs:
    #     res.append(doc._data)
    # return jsonify(res)

@functions_framework.http
def execute_algorithm(request):
    return execute_algorithm_by_id(request)