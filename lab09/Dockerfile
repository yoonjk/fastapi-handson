FROM python:3.11.9-slim
ENV PORT 8000
WORKDIR /app
# Create virtual environment
RUN python3 -m venv /ve

# Enable venv
ENV PATH="/ve/bin:$PATH"

# Copy requirements file
ADD requirements.txt .

# Copy source to target in docker
COPY . . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE $PORT

CMD uvicorn --host=0.0.0.0 --port $PORT  main:app
