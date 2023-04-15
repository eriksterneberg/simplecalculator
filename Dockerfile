FROM python:3.11

RUN mkdir -p /simplecalculator/
COPY main.py /
COPY /simplecalculator/ /simplecalculator/
COPY /tests/test*.txt /
