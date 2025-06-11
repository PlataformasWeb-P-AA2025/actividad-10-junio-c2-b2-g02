from flask import render_template, request
from app import app

@app.route("/", methods=["GET", "POST"])
def hello():
    name = "Invitado"
    if request.method == "POST":
        name = request.form.get("name", "Invitado")
    return render_template("hello.html", name=name)
