install:
	poetry install

presentation:
	poetry run jupyter lab EmissionDataAnalysis.ipynb


update-requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt
