cd src
call %~dp0\virtual_env\Scripts\activate.bat
start "" functions_framework --target=hello --port=5000
start "" functions_framework --target=bye --port=5001








