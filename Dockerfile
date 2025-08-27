FROM python:3.10-slim

WORKDIR /app
COPY requirements-prod.txt .

# Install production requirements
RUN pip install --no-cache-dir --default-timeout=100 -r requirements-prod.txt \
    && rm -rf /root/.cache/pip

# Download NLTK data
RUN python -m nltk.downloader stopwords wordnet

COPY . .
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--timeout", "120"]