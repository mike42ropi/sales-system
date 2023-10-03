import psycopg2
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')
from flask import Flask, render_template
from dbservice import myduka_
from flask import request, redirect

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/products", methods=['GET', 'POST'])
def products():
    p = myduka_("products","sales")
    sp = p.get_data()
    if request.method == "POST":
           cursor = conn.cursor()
           prod_n= request.form['product_name']
           buy_p= request.form['buying_price']
           sell_p= request.form['selling_price']
           stock_q= request.form['stock_quantity'] 
           columns = "(product_name,buying_price,selling_price,stock_quantity)"
           valuess=(prod_n,buy_p,sell_p,stock_q)
           w = f"INSERT INTO products {columns} VALUES {valuess}"
           cursor.execute(w)
           conn.commit()
           cursor.close
    
    return render_template("products.html", myprods = sp)

@app.route("/sales")
def sales():
    s = myduka_("products","sales")
    sp1 = s.get_data1()
    return render_template("sales.html", myprods1 = sp1)
app.run()