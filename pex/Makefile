init:
	virtualenv -p python3 env
	env/bin/python -m pip install -r requirements.txt

build:
	env/bin/python setup.py sdist
	env/bin/pex myapp -o myapp.pex -e 'myapp.app' -f dist -v
