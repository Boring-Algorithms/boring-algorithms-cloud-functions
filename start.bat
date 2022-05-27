cd src
call %~dp0\virtual_env\Scripts\activate.bat
start "" functions_framework --target=get_alrotithms --port=5000 --debug
start "" functions_framework --target=execute_algorithm --port=5001 --debug
start "" functions_framework --target=execute_test_suite --port=5002 --debug
start "" functions_framework --target=get_test_suites --port=5003 --debug
start "" functions_framework --target=drop_collection --port=5004 --debug









