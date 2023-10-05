import psycopg2
from flask import Flask, render_template, request, redirect
from dbservice import insert_data, insert_data1, get_data, get_data1
from datetime import datetime

# Establish a database connection
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add_products", methods=['POST'])
def add_products():
    prod_n = request.form['product_name']
    buy_p = request.form['buying_price']
    sell_p = request.form['selling_price']
    stock_q = request.form['stock_quantity'] 

    values = (prod_n, buy_p, sell_p, stock_q)

    try:
        insert_data(values)
        return redirect("/products")
    except Exception as e:
        # Handle the exception, e.g., log it or return an error page
        return render_template("error.html", message=str(e))

@app.route("/products", methods=['GET', 'POST'])
def products():
    try:
        sp = get_data("products")
        return render_template("products.html", myprods=sp)
    except Exception as e:
        # Handle the exception, e.g., log it or return an error page
        return render_template("error.html", message=str(e))

@app.route("/add_sales", methods=['POST'])
def add_sales():
    pid = request.form['pid']
    quan = request.form['quantity']
    crea_at = datetime.now().replace(microsecond=0)
    v1 = (pid, quan, crea_at)

    try:
        insert_data1(v1)
        return redirect("/sales")
    except Exception as e:
        # Handle the exception, e.g., log it or return an error page
        return render_template("error.html", message=str(e))

@app.route("/sales", methods=['GET', 'POST'])
def sales():
    try:
        ss = get_data("products")
        sp1 = get_data1("sales")
        return render_template("sales.html", myprods1=sp1, prd=ss)
    except Exception as e:
        # Handle the exception, e.g., log it or return an error page
        return render_template("error.html", message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
