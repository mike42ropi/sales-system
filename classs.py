import psycopg2
from flask import request, redirect
from main import products
from main import add_products
conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')





class myduka_:
   records=[]
   records1=[]
   ins_bool = False
   
   def get_data(self,products):
        

        cursor = conn.cursor()
        
        cursor.execute(self.records.append("select * from" +" "+ products))

        self.data1 = cursor.fetchall()
        return self.data1
   
   def get_data1(self,sales):
        

        cursor = conn.cursor()
        cursor.execute(self.records.append("select * from" +" "+ sales))

        self.data2 = cursor.fetchall()
        return self.data2 


   def insert_data(products):
    try:
        cursor = conn.cursor()
        columns = "(product_name,buying_price,selling_price,stock_quantity)"
                  
        cursor.execute(f"INSERT INTO {products}{columns} VALUES")
        ins_bool= True
        conn.commit()
    except:
 
        pass
    



prosa=myduka_("products","sales")

# conn.close()