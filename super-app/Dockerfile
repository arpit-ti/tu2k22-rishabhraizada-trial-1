FROM python:slim

# WORKDIR /${MYDIR} 

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

# # Variable for directory
# COPY app-1/ .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", $PORT, "--reload"]