import psycopg2

conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='sequence150')

def get_data(table_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_data1(table_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def insert_data(values):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO products (product_name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

def insert_data1(values1):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO sales (pid, quantity, created_at) VALUES (%s, %s, %s)"
        cursor.execute(query, values1)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()


def profit(sales,products):
    cursor = conn.cursor()
    m =" SELECT SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit ,\
    sales.created_at FROM sales JOIN products  ON sales.pid = products.id\
    WHERE sales.created_at >= '2023-08-07 11:33:08' OR sales.created_at <='2023-10-05 09:29:27'\
    GROUP BY  sales.created_at;"

    cursor.execute(m)
    data3=cursor.fetchall()
    return data3



# conn.close()