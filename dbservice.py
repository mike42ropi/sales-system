import psycopg2
from datetime import datetime
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')
def get_data(p):
    

    cursor = conn.cursor()
    t="select * from" +" "+ p

    cursor.execute(t)


    data = cursor.fetchall()
    
    
    return data



prods=get_data("products")
print(prods)

sale1s=get_data("sales")
print(sale1s)





conn = psycopg2.connect(
     database="myduka_class", user='postgres', password='sequence150')

def add_data1(p,s):
    conn.autocommit = True
    cursor = conn.cursor()
    date1= datetime.now().replace(microsecond=0)
    columns="(product_name, buying_price, selling_price, stock_quantity)"
    valuess="('lotion',60,100,10)"
    columns1="(pid,quantity,created_at)"
    valuess1=f"(31,2.00,'{date1}')"
    w =f"INSERT INTO {p} {columns} VALUES {valuess}"
    l =f"INSERT INTO {s} {columns1} VALUES {valuess1}"

    cursor.execute(w)
    cursor.execute(l)

conn.commit()
 
    
    
 
bwx=add_data1("products","sales")

# bwx=add_data1()
conn.close()

