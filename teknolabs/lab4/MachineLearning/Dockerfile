FROM python:3.8-slim

WORKDIR /app

COPY app.py music_recommender.joblib requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]