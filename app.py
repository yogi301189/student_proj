from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect(url_for("form"))
    return render_template("login.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        session["data"] = {
            "name": request.form["name"],
            "fees": request.form["fees"],
            "department": request.form["department"],
            "trainer": request.form["trainer"]
        }
        return redirect(url_for("table"))
    return render_template("form.html")

@app.route("/table")
def table():
    return render_template("table.html", data=session.get("data"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
