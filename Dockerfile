FROM python:3.8

ARG PORT

ENV PORT=${PORT} \
    HOST=0.0.0.0

EXPOSE $PORT

WORKDIR /code

# Creating folders, and files for a project:
COPY . .

RUN pip install dist/*.whl \
    && rm -rf dist

CMD ["python", "run.py"]