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





# 2


def add_data1(p,s):
    conn.autocommit = True
    cursor = conn.cursor()
    date1= datetime.now().replace(microsecond=0)
    columns="(product_name, buying_price, selling_price, stock_quantity)"
    valuess="('hand lotion',60,100,10)"
    columns1="(pid,quantity,created_at)"
    valuess1=f"(32,2.00,'{date1}')"
    w =f"INSERT INTO {p} {columns} VALUES {valuess}"
    l =f"INSERT INTO {s} {columns1} VALUES {valuess1}"

    cursor.execute(w)
    cursor.execute(l)

conn.commit()
bwx=add_data1("products","sales")





# 3


def rem_stock(p,s):
    cursor = conn.cursor()
    m =f"SELECT {p}.product_name,SUM({p}.stock_quantity-{s}.quantity) AS rem_stock from {s}  JOIN products  ON {s}.pid = {p}.pid GROUP BY {p}.product_name ORDER BY rem_stock"

    cursor.execute(m)


    data = cursor.fetchall()
    
    
    return data

prods=rem_stock("products","sales")
print(prods)



conn.close()

