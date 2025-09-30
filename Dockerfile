FROM python:3.13.7-slim-bookworm

WORKDIR workspace
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver"]

