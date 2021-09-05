FROM python:3.8

ARG PORT

ARG HOST

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.8 \
    PORT=${PORT} \
    HOST=${HOST}

EXPOSE $PORT

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi --no-dev

# Creating folders, and files for a project:
COPY . /code

CMD ["python", "run.py"]