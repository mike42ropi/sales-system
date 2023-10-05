import psycopg2
from flask import request, redirect
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')






   
def get_data(products):
    cursor = conn.cursor()
        
    cursor.execute("select * from" +" "+ products)

    data1 = cursor.fetchall()
    return data1
prosa=get_data("products")
   
def get_data1(self,sales):
    cursor = conn.cursor()
    cursor.execute("select * from" +" "+ sales)
    data2 = cursor.fetchall()
    return data2 
prosa=get_data1("sales")

def insert_data(products):
    try:
        cursor = conn.cursor()
        columns = "(product_name,buying_price,selling_price,stock_quantity)"
                  
        cursor.execute(f"INSERT INTO {products}{columns} VALUES ")
        ins_bool= True
        conn.commit()
    except:
 
        pass
    
prosa=insert_data("products")




# conn.close()