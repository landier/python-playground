init:
	virtualenv -p python3 env
	. env/bin/activate
	pip install -r requirements.txt

build: init
	python setup.py bdist_wheel
