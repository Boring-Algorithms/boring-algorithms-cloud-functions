cd src
call %~dp0\virtual_env\Scripts\activate.bat
start "" functions_framework --target=hello --port=5000 --debug
start "" functions_framework --target=bye --port=5001 --debug
start "" functions_framework --target=get_alrotithms --port=5002 --debug
start "" functions_framework --target=execute_algorithm --port=5003 --debug








