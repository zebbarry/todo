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

# Copy only requirements to cache them in docker layer
WORKDIR /code

COPY dist /code/dist

RUN pip install dist/*.whl \
    && rm -rf dist

# Creating folders, and files for a project:
COPY . /code

CMD ["python", "run.py"]