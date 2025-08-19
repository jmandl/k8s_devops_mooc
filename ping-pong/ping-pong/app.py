from flask import Flask
import os

if not os.path.exists('/app/ping-pong/counter.txt'):
    counter = 0
else:
    with open('/app/ping-pong/counter.txt', 'r') as f:
        contentfile = f.read()
        counter = int(contentfile.strip())

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/pingpong')
def index():
    global counter
    counter += 1
    with open('/app/ping-pong/counter.txt', 'w') as f:
        f.write(str(counter))
    return f"pong {counter}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)