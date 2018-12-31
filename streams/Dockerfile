FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD main.py main.py
ADD __init__.py __init__.py
EXPOSE 6666

CMD  ["faust", "-A", "main", "worker", "-l", "info"]
