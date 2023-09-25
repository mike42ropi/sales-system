import psycopg2
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')
def get_data(p):
    

    cursor = conn.cursor()
    t="select * from" +" "+ p

    cursor.execute(t)


    data = cursor.fetchall()
    
    
    return data



prods=get_data("products")
print("products is:",prods)

conn = psycopg2.connect(
     database="myduka_class", user='postgres', password='sequence150')
def get_data1(s):
     

     cursor = conn.cursor()

     d="select * from " + " "+s
     cursor.execute(d)


     data1 = cursor.fetchall()
    
    
     return data1
     

sale1s=get_data1("sales")
print("sales is:",sale1s)
conn.close()