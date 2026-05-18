FROM python:3.11-slim

# Install system utilities
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy and install Python packages
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install Chromium and its necessary OS dependencies
RUN pip install playwright && playwright install chromium
RUN playwright install-deps chromium

COPY . .

# Hugging Face routes traffic through port 7860 by default
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
