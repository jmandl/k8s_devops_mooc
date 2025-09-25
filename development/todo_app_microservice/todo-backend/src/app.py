import os
from flask import Flask, render_template, request

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
                todos.append(line.strip())
    else:
        todos = []

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/todos', methods=["GET", "POST"])
def index():
    global todos

    if request.method == "POST":
        todo_item = request.form.get("todo")
        if len(todo_item) <= 140:
            append_to_file(todo_item)
        read_todos()
        return todos
    else:
        read_todos()
        return todos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)