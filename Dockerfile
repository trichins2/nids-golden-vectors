# 1. start from an official base image (Debian + Python 3.12)
ARG PY=3.12
FROM python:${PY}-slim
# 2. like `cd /app`, created if missing
WORKDIR /app
# 3. copy ONLY the dependency list first...
COPY requirements.txt .
# 4. ...and install it
RUN pip install --no-cache-dir -r requirements.txt
# 5. now copy the rest of your code
COPY . .
# 6. default command when the container starts
CMD ["python", "-m", "pytest", "-q"]
# -m adds the current folder to Python's import path
