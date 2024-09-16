start_dev_server:
	fastapi dev ./car_data_api/app.py

venv:
	poetry shell

blt:
	./build.sh