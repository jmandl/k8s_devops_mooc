import os
import requests
from datetime import datetime, timedelta
from flask import Flask, render_template

def download_picture():
    image_url = 'https://picsum.photos/250'
    response = requests.get(image_url)
    if response.status_code == 200:
        with open('static/random.jpg', 'wb') as f:
            f.write(response.content)

app = Flask(__name__)

old_time = datetime.now()
download_picture()

PORT = int(os.getenv("PORT", 5000))

@app.route('/')
def index():
    global old_time
    current_time = datetime.now()
    time_difference = current_time - old_time
    if time_difference >= timedelta(minutes=10):
        download_picture()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)