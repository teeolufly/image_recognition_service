FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into container
COPY . .

# Expose service port
EXPOSE 8000

# start application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]