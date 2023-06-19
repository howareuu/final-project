install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv tests

format:
	black *.py

lint:
	pylint --disable=R,C main.py

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 787163628025.dkr.ecr.us-east-1.amazonaws.com
	docker build -t mlops-final-project .
	docker tag mlops-final-project:latest 787163628025.dkr.ecr.us-east-1.amazonaws.com/mlops-final-project:latest
	docker push 787163628025.dkr.ecr.us-east-1.amazonaws.com/mlops-final-project:latest

all: install format lint test deploy