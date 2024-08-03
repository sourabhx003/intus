# STEP 1: Install base image. Optimized for Python.
FROM python:3.10-slim-buster

# Step 2: Add requirements.txt file 
COPY requirements.txt /requirements.txt

# Step 3:  Install required python dependencies from requirements file
RUN pip install -r requirements.txt

# Step 4: Copy source code in the current directory to the container
ADD . /app

# Step 5: Set working directory to previously added app directory
WORKDIR /app

# Step 6: Expose the port Flask is running on
# Default fastapi runs in port : 8000
EXPOSE 8000

# Step 9: Run Flask
# CMD ["fastapi","run"]
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]