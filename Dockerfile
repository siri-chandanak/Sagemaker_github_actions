FROM python:3.11-slim

WORKDIR /app

COPY inference/iris_model.pkl .
COPY inference/inference.py .

RUN pip install --no-cache-dir scikit-learn pandas flask gunicorn

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "inference:app"]
