
from flask import escape
import functions_framework

from functions.security import *
from functions.database_manager import *

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

headers = {
    'Access-Control-Allow-Origin': '*'
}

@functions_framework.http
def get_alrotithms(request):
    try:
        return get_algorithms_dict(), 200, headers
    except Exception as e:
        return f"Bad Request - {e}", 400, headers

@functions_framework.http
def execute_algorithm(request):
    try:
        id = request.json["algorithm_id"]
        data = request.json["data"]
        return execute_algorithm_by_id(id, data), 200, headers
    except Exception as e:
        return f"Bad Request - {e}", 400

@functions_framework.http
def get_test_suites(request):
    try:
        return get_available_test_suites(), 200, headers
    except Exception as e:
        return f"Bad Request - {e}", 400

@functions_framework.http
def execute_test_suite(request):
    try:
        algo_id = request.json["algorithm_id"]
        suite_id = request.json["test_suite_id"]
        return execute_test_suite_function(algo_id, suite_id, db), 200, headers
    except Exception as e:
        return f"Bad Request - {e}", 400

@functions_framework.http
def drop_collection(request):
    try:
        if(not secret_token_valid(request.json["secret_key"])):
            return "Token not valid", 401
        else:
            collection = request.json["collection"]
            return delete_collection(db, collection), 200, headers
    except Exception as e:
        return f"Bad Request - {e}", 400
    
@functions_framework.http
def get_test_executions(request):
    try:
        return get_all_test_executions(db, request), 200, headers
    except Exception as e:
        return f"Bad Request - {e}", 400