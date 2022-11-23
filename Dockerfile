FROM python:3

COPY deployment.py /deployment.py

CMD ["python", "/deployment.py"]
