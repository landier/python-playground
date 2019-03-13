init:
	virtualenv -p python3 env
	. env/bin/activate
	pip install -r requirements.txt

build:
	. env/bin/activate
	python setup.py sdist
	pex -r $(pip freeze) myapp -o myapp.pex -e 'myapp.app' -f dist -v
