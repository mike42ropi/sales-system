from flask import Flask, render_template
from dbservice import myduka_

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/products")
def products():
    p = myduka_("products","sales")
    sp = p.get_data()
    return render_template("products.html", myprods = sp)

@app.route("/sales")
def sales():
    return render_template("sales.html")
app.run()