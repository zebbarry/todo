FROM python:3.8-slim

ARG PORT

ENV PORT=${PORT} \
    HOST=0.0.0.0

EXPOSE $PORT

WORKDIR /project

# Copy only requirements to cache them in docker layer
COPY requirements.txt .

# Project initialization:
RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . .

CMD ["python", "run.py"]