FROM python:3.8-slim

RUN pip install pytest

COPY ./2020 /advent_of_code/2020
