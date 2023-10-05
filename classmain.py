import psycopg2  
from flask import Flask, render_template, request, redirect, g
from dbservice import myduka_
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add-products", methods=['POST'])
def add_products():

    prod_n= request.form['product_name']
    buy_p= request.form['buying_price']
    sell_p= request.form['selling_price']
    stock_q= request.form['stock_quantity'] 

    v=(prod_n,buy_p,sell_p,stock_q)
    db= myduka_("products","sales")
    db.insert_data(v)      
    if db.ins_bool == True:
        return redirect("/products")


@app.route("/products")
def products():       
    db = myduka_("products")
    db.get_data("products")
    sp = db.records

    return render_template("products.html", myprods = sp)


@app.route("/sales")
def sales():
    db = myduka_("sales")
    db.get_data1("sales")
    sp1 = db.records1
    return render_template("sales.html", myprods1 = sp1)

if __name__ == '__main__':
    app.run(debug=True)