
from .algorithm_manager import *
from .sort_algorithms import *
import json

test_suites = {
    "array_of_numbers": {
        "name": "array_of_numbers",
        "description": "Test suite of multiple array of numbers."
    },
    "array_of_letters": {
        "name": "array_of_letters",
        "description": "Test suite of multiple array of letters."
    }
}

check_functions_dict = {
    "array_of_numbers": check_is_sorted
}

def execute_test_suite_function(algorithm_id, test_suite, db):
    test_data = get_test_data(test_suite)
    res = {"executions": [], "invalid_tests_count": 0, "algorithm_id": algorithm_id, "test_suite": test_suite, "amount_of_tests": 0}
    for data in test_data:
        execution = execute_algorithm_by_id(algorithm_id, data).json
        res["executions"].append(execution["execution_time"])
        res["amount_of_tests"] += 1
        if(not check_functions_dict[test_suite](execution["algorithm_response"])):
            res["invalid_tests_count"] += 1
    insert_test_execution_into_db(db, res)
    return jsonify(res)

def get_test_data(type):
    if(type == "array_of_numbers"):
        return get_basic_sort_test_suite()
    else:
        return ""

def get_basic_sort_test_suite():
    return [
        [0, 10, 5],
        [0, 100, 2, 4, 44, 451, 132],
        [0, 10, 5]
    ]

def get_available_test_suites():
    return json.dumps(test_suites)

def insert_test_execution_into_db(db, res):
    db.collection(u'test_suite_executions').add(res)

def get_all_test_executions(db, request):
    res = []
    users_ref = db.collection(u'test_suite_executions')
    docs = users_ref.stream()

    for doc in docs:
        obj = doc.to_dict()
        obj["id"] = doc.id
        res.append(obj)
    return jsonify(res)