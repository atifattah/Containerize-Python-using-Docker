FROM python:3.11-slim

ADD main.py .

RUN pip install scikit-learn

CMD ["python", "./main.py"]