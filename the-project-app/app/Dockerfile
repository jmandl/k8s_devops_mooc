FROM python:3.13-slim
WORKDIR /app
COPY src/ .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-u", "/app/app.py"]