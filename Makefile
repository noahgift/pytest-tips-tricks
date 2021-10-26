install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting tests
	python -m pytest --nbval notebook.ipynb	#tests our jupyter notebook
format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test format