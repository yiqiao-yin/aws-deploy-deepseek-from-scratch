# Use official Python image as a base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy local files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Define the entry point command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
