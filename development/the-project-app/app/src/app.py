import os
import requests
from datetime import datetime, timedelta
from flask import Flask, render_template, request
import psycopg2

def download_picture():
    image_url = os.getenv("image_picture", "https://picsum.photos/250")
    response = requests.get(image_url)
    if response.status_code == 200:
        with open('static/random.jpg', 'wb') as f:
            f.write(response.content)


def db_connection():
    conn = psycopg2.connect(
        host="theprojectdbsvc",
        database="mydb",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

conn = db_connection()
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE theproject (todos VARCHAR(145))')
    conn.commit()
except:
    print('table already exists!')


def append_to_file(todo_item):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO theproject (todos)''VALUES (%s)', (todo_item,))
    conn.commit()

def read_todos():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM theproject')
    todos = cur.fetchall()
    return list(map(lambda todo:todo[0], todos))

app = Flask(__name__)

old_time = datetime.now()
download_picture()

PORT = int(os.getenv("PORT", 5000))

@app.route('/', methods=["GET", "POST"])
def index():
    global old_time

    current_time = datetime.now()
    time_difference = current_time - old_time
    if time_difference >= timedelta(minutes=10):
        download_picture()

    if request.method == "POST":
        todo_item = request.form.get("todo")
        if len(todo_item) <= 140:
            append_to_file(todo_item)
        else:
            print("todo bigger than 140 caracters")
        todos = read_todos()
        return render_template('index.html', todos=todos)
    else:
        todos = read_todos()
        return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)