from flask import Flask
import os

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/')
def index():
    try:
        with open('/app/log/log.txt', 'r') as f:
            file_content = f.read()
        return file_content
    except FileNotFoundError:
        return('Could not find the file /app/log/log.txt in folder.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)