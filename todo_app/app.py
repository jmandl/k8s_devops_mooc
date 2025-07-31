from flask import Flask
import os

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/')
def index():
    return f"Server started in port {PORT}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)