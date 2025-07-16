from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

@app.route("/tasks")
def tasks():
    r = requests.get("http://127.0.0.1:5000/uzduotys")
    tasks = r.json()
    return render_template("tasks.html", tasks=tasks)

@app.route("/tasks/<int:id>")
def task(id):
    r = requests.get(f"http://127.0.0.1:5000/uzduotys/{id}")
    task = r.json()
    return render_template("task.html", task=task)


@app.route("/tasks/new", methods=['GET', "POST"])
def new_task():
    if request.method == "POST":
        payload = {
            "pavadinimas": request.form['title'],
            "atlikta": False
        }
        r = requests.post("http://127.0.0.1:5000/uzduotys/nauja", json=payload)
        return redirect("/tasks")
    return render_template("task_new.html")


if __name__ == '__main__':
    app.run(port=8000, debug=True)