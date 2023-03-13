FROM python:3.10-slim-buster
LABEL maintainer="Jessica Walkenhorst"
LABEL description="Nautical Carbon Emission Analyis"

ARG PIP_VERSION="21.2.1"
ARG POETRY_VERSION="1.2.0"

RUN pip3 install -q "pip==$PIP_VERSION"
RUN pip3 install -q "poetry==$POETRY_VERSION"

WORKDIR /home/

COPY pyproject.toml poetry.lock ./
#COPY src ./src/
COPY EmissionDataAnalysis.ipynb .
COPY data ./data/

RUN poetry install --no-dev

EXPOSE 8866

#ENTRYPOINT ["poetry", "run", "jupyter", "lab", "--allow-root", "--no-browser", "--ServerApp.token=abcd"allow]
ENTRYPOINT ["poetry", "run", "voila", "--port=8866",  "--Voila.ip=0.0.0.0", "--no-browser", "EmissionDataAnalysis.ipynb"]
