FROM python:3.9-slim
WORKDIR /genealogy
COPY reqs.txt .
RUN pip install -r reqs.txt
COPY . .
CMD ["python", "main.py"]