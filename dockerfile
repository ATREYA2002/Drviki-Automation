# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list first and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual application code
COPY . .

# Expose the app port
EXPOSE 8080

# Run the app with gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]
