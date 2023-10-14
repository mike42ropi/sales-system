import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')


from flask import Flask, render_template, request, redirect,url_for,session,flash

from dbservice import insert_data,insert_data1,get_data,get_data1,profit,check_email,email_pass,create_user
from datetime import datetime

app = Flask(__name__)
app.secret_key="mike42ropi!" 


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'post':
        
        email = request.form['email']
        password = request.form['password']
        
        log_in= email_pass(email,password)
        if log_in:
            session["log_in"] = log_in[0]
            return redirect("/dashboard") 
        else:
            flash("Invalid Email or Password")
    return render_template("login.html")

def email_pass(email,password):
    cursor = conn.cursor()
    check_all = 'SELECT id,full_name FROM users WHERE email = %s AND password = %s'

    cursor.execute(check_all,(email,password))
    
    data5=cursor.fetchone()
    # if log_in:
        
    #     if log_in != None:  
    #         return log_in
    return data5 

def insert_data1(values1):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO sales (pid, quantity, user_id,created_at) VALUES (%s, ,%s,%s, %s)"
        cursor.execute(query, values1)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()
# crea_at= datetime.now().replace(microsecond=0)
values1= (4,20,3.crea_at)

