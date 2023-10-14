# data = [(1, )]


# selected_integers = data[0][0]




# # Access the first (and only) tuple in the list and then access its first element (index 0)


# print(selected_integers)

# sales=[{"sales_one":[23,45,76,48]},
#       {"sales_two":[44,20,17,34]},
#       {"sales_three":[89,32,12,34]}]
# avg_sales1=(sales[0].get("sales_one")[0]+sales[0].get("sales_one")[1]+sales[0].get("sales_one")[2]+sales[0].get("sales_one")[3])/len(sales[0].get("sales_one"))
# avg_sales2=(sales[1].get("sales_two")[0]+sales[1].get("sales_two")[1] +sales[1].get("sales_two")[2]+sales[1].get("sales_two")[3])/len(sales[1].get("sales_two"))
# avg_sales3=(sales[2].get("sales_three")[0]+sales[2].get("sales_three")[1] +sales[2].get("sales_three")[2]+sales[2].get("sales_three")[3])/len(sales[2].get("sales_three"))
# avg_sales =[]
# avg_sales.append(avg_sales1)
# avg_sales.append(avg_sales2)
# avg_sales.append(avg_sales3)
# print(avg_sales)

# for dict in sales:
#     for key,values in dict.items():
#         total=sum(values)/len(values)
#         print(total)
sales=[{"sales_one":[23,45,76,48]},
      {"sales_two":[44,20,17,34]},
      {"sales_three":[89,32,12,34]}]

avg_sales=[]
for a in sales:
    for k,v in a.items():
        avg =sum(v)/len(v)
        avg_sales.append(avg)
print(avg_sales)
        