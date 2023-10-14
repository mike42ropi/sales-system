import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')





# class myduka_:
   
#     def __init__(self,products,sales):
#         self.products=products
#         self.sales=sales
#         self.add_data1()
#         self.add_data2()
#         self.rem_stock()
        
     
    
#     def add_data1(self):
            
#         cursor = conn.cursor()
        
#         columns = "(product_name,buying_price,selling_price,stock_quantity)"
#         valuess = f"{vp}"
        
#         w = f"INSERT INTO {self.products} {columns} VALUES {valuess}"


#         cursor.execute(w)
#         conn.commit()

              

#     def add_data2(self):
          
#         cursor = conn.cursor()
#         date1 = datetime.now().replace(microsecond=0)
   
#         columns1 = "(quantity,created_at)"
#         valuess1 = f"({vs},'{date1}')"
 
#         l = f"INSERT INTO {self.sales} {columns1} VALUES {valuess1}"

   
#         cursor.execute(l)
#         conn.commit()



#     def rem_stock(self):
#         cursor = conn.cursor()
#         m =f"SELECT {self.products}.product_name,SUM({self.products}.stock_quantity-{self.sales}.quantity)\
#         AS rem_stock from {self.sales}  JOIN products  ON {self.sales}.pid = {self.products}.id GROUP BY\
#         {self.products}.product_name ORDER BY rem_stock"

#         cursor.execute(m)


#         self.data3=cursor.fetchall()
#         return self.data3
        

# vp =  (input("Enter Product name: "),
#        float(input("Enter buying_price: ")), 
#        float(input("Enter selling_price: ")),
#        float(input("Enter Stock quantity: ")))

# vs = float(input("Enter a quantity: "))

# prosa=myduka_("products","sales")


# conn.close()
# def check_email(email):
#     cursor = conn.cursor()
#     check = f"SELECT * FROM users WHERE email='{email}'"
#     cursor.execute(check,email)
#     data4=cursor.fetchone()
    
 

# a=check_email("jinja@gmail.com")
# print(a)
def create_user(values):
    cursor = conn.cursor()
    insert_query = "INSERT INTO users(full_name,email,password) VALUES('martin koech','mkoech@gmail.com','agfgsj')"
    cursor.execute(insert_query)
    conn.commit()
