
from .sort_algorithms import *
from flask import jsonify
import json
from timeit import Timer

algorithm_to_function = {
    "python_sort": python_sort
}

algorithm_dict = {
    "python_sort": {
        "name": "python_sort",
        "type": "sort",
        "created_by": "python"
    }
}


def get_algorithms_dict():
    return json.dumps(algorithm_dict)

def execute_algorithm_by_id(id, data):

    if(id not in algorithm_to_function):
        return jsonify({"message": "Algorithm does not exist"}), 404

    res = {}
    algorithm_response = []
    timer = Timer(lambda: algorithm_response.append(algorithm_to_function[id](data)))
    response_time = timer.timeit(1)
    res["message"] = "Algorithm executed successfully"
    res["algorithm_response"] = algorithm_response
    res["execution_time"] = '%f' % response_time
    return jsonify(res)    