clean-code:
	./bin/run-isort.sh
	./bin/run-black.sh
	./bin/run-flake8.sh

image:
	docker build -t nautical-carbon-emission-analysis:latest .

install:
	poetry install

test:
	poetry run pytest tests/

presentation:
	poetry run jupyter lab EmissionDataAnalysis.ipynb

update-requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt

