import os
import requests
from datetime import datetime, timedelta
from flask import Flask, render_template, request

def download_picture():
    image_url = 'https://picsum.photos/250'
    response = requests.get(image_url)
    if response.status_code == 200:
        with open('static/random.jpg', 'wb') as f:
            f.write(response.content)


todos_file_path = "static/todos.json"

def append_to_file(todo_item):
    with open(todos_file_path, "a") as file:
        file.write(f"{todo_item}\n")

def read_todos():
    global todos_file_path
    global todos
    todos = []
    if os.path.exists(todos_file_path):
        with open("static/todos.json", "r") as file:
            for line in file.readlines():
                todos.append(line)
    else:
        todos = []

app = Flask(__name__)

old_time = datetime.now()
download_picture()

PORT = int(os.getenv("PORT", 5000))

@app.route('/', methods=["GET"])
def index():
    global old_time
    global todos

    current_time = datetime.now()
    time_difference = current_time - old_time
    if time_difference >= timedelta(minutes=10):
        download_picture()

    backend_result = requests.get('http://todo-backend:5000/todos')

    return render_template('index.html', todos=backend_result.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)