import psycopg2


conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')





class myduka_:
   
    def __init__(self,products,sales):
        self.products=products
        self.sales=sales
        self.get_data()
        self.get_data1()
     
    
    def get_data(self):
        

        cursor = conn.cursor()

        t="select * from" +" "+ self.products
        
        cursor.execute(t)

        self.data1 = cursor.fetchall()
        return self.data1



    def get_data1(self):
        

        cursor = conn.cursor()
        t="select * from" +" "+ self.sales
        

        cursor.execute(t)


        self.data2 = cursor.fetchall()
        return self.data2 



prosa=myduka_("products","sales")

# conn.close()