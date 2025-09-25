FROM python:3.13-slim
WORKDIR /app
COPY cron.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-u", "/app/cron.py"]
