from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/products")
def products():
    return render_template("sales.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")
app.run()