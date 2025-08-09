from flask import Flask
import os

counter = 0

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/pingpong')
def index():
    global counter
    counter += 1
    return f"pong {counter}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)