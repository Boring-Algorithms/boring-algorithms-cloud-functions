
from flask import escape
import functions_framework

from algorithms.sort_algorithms import *
from algorithms.algorithm_manager import *
from algorithms.algorithm_tests_manager import *

from dotenv import load_dotenv
load_dotenv()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@functions_framework.http
def get_alrotithms(request):
    return get_algorithms_dict()

@functions_framework.http
def execute_algorithm(request):
    id = request.json["algorithm_id"]
    data = request.json["data"]
    return execute_algorithm_by_id(id, data)

@functions_framework.http
def get_test_suites(request):
    return get_available_test_suites()

@functions_framework.http
def execute_test_suite(request):
    algo_id = request.json["algorithm_id"]
    suite_id = request.json["test_suite_id"]
    return execute_test_suite_function(algo_id, suite_id)