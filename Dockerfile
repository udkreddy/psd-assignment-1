FROM python:3.8-slim
WORKDIR /usr/src/app
COPY sparse_recommender.py .
COPY test.py .
COPY requirements.txt .
CMD [ "python", "./sparse_recommender.py" ]