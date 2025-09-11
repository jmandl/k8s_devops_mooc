from flask import Flask
import os
import uuid
from datetime import datetime, timezone

def generate_uuid_loop():
    return uuid.uuid4()

def get_utc_timestamp():
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

if not os.path.exists('/app/counter.txt'):
    counter = 0
else:
    with open('/app/counter.txt', 'r') as f:
        contentfile = f.read()
        counter = int(contentfile.strip())

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/pingpong')
def index():
    timestamp = get_utc_timestamp()
    new_uuid = generate_uuid_loop()
    
    message = os.getenv("MESSAGE", "Message is null")
    with open('/app/static/file.txt', 'r') as f:
        message_in_file = f.read()

    global counter
    counter += 1
    with open('/app/counter.txt', 'w') as f:
        f.write(str(counter))
    return f"""
    file content: {message_in_file}
    env variable: MESSAGE={message}
    {timestamp}: {new_uuid}.
    Ping / Pongs: {counter}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)