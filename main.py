
from flask import Flask, render_template, request, redirect,url_for,session,flash

from dbservice import insert_data,insert_data1,get_data,get_data1,profit,check_email,email_pass,create_user
from datetime import datetime



app = Flask(__name__)
app.secret_key="mike42ropi!" 

# def login_check():
#   if session['email']!= None:
#     return redirect(url_for("profit1"))
#   return redirect(url_for("login"))

# @app.route("/sales")
# def sales():
#   login_check
#   session['email']

#   return render_template("index.html") 

@app.route("/")
def index():
  return render_template("index.html") 


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        email = request.form.get('email')
        password = request.form.get('password')
        
        log_in= email_pass(email,password)
        if log_in:
            session["log_in"] = log_in[0]
            return redirect("/dashboard") 
        else:
            flash("Invalid Email or Password")
    return render_template("login.html")
    


# @app.route("/register", methods=['GET','POST'])
# def register():
#     email_2 = request.form.get('email_2')
#     user_n2 = request.form.get('full_name_2')
#     passd2 = request.form.get('password_2')
#     reg1 = (email_2, user_n2, passd2)
    
#     return create_user(reg1) 
   
@app.route("/register", methods=["GET","POST"])
def register1():
    full_name = request.form.get('full_name_2')
    email = request.form.get('email_2')
    password = request.form.get('password_2')
    reg1=(full_name, email, password)
    if full_name != None and email != None and password != None:
       create_user(reg1)

    else:
        pass   
    return redirect("/login")

@app.route("/dashboard")
def profit1():       
    p1=[float(i[0]) for i in profit()]
    p2=[str(i[1]) for i in profit()]

    
    return render_template("dashboard.html", myprof = p1, myprof2=p2)


@app.route("/add_products", methods=['POST'])
def add_products():
    
    prod_n=request.form['product_name']
    buy_p=request.form['buying_price']
    sell_p=request.form['selling_price']
    stock_q=request.form['stock_quantity'] 

    values=(prod_n,buy_p,sell_p,stock_q)
        
    insert_data(values)
       
    return redirect("/products")


@app.route("/products",methods=['GET', 'POST'])
def products():       
    sp=get_data("products")
    
    return render_template("products.html", myprods = sp)

@app.route("/add_sales" , methods=['POST'])
def add_sales():
    pid= request.form['pid']
    quan= request.form['quantity']
    crea_at= datetime.now().replace(microsecond=0)

    values1=(pid,quan,crea_at)
            
    insert_data1(values1)
    return redirect("/sales")


@app.route("/sales", methods=['GET', 'POST'])
def sales():
    ss=get_data("products")
    sp1=get_data1("sales")
    return render_template("sales.html", myprods1 = sp1,prd=ss)


@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop("reg1", None)
    return redirect('/')


# @app.route('/sales1',methods = ["GET","POST"])  
# def quanti():  
#     error = None;  
#     if request.method == "POST":  
#         if request.form['quantity'] > 50:  
#             error = "quantity should be below or equal to 50" 
#         else:  
#             flash("") 
#             return redirect(url_for('sales'))  
#     return render_template('sales.html',error=error)  

app.run(debug=True)

