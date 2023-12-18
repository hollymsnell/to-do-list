from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/todos.json")
def index():
    return db.todos_all()

@app.route("/todos.json", methods=["POST"])
def create():
    task = request.form.get("task")
    due_date = request.form.get("due_date")
    priority = request.form.get("priority")
    status = request.form.get("status")
    return db.todos_create(task, due_date, priority, status)