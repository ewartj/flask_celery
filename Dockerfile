FROM python:3.10.14


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    redis-server \
    supervisor && \
    rm -rf /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt analysis_app.py .

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app /app/app

# Expose the Flask application port
EXPOSE 5005

CMD ["/usr/bin/supervisord"]