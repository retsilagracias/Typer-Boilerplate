FROM python:3.9.1-slim-buster
ADD ./src/requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD ./src /app/
RUN pip install -e /app/horoscopecli
ENTRYPOINT ["python", "/app/horoscopecli/horoscopecli/main.py"]