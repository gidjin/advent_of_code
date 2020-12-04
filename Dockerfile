FROM python:3.8-slim

RUN pip install pytest

COPY . /advent_of_code/
