# import pandas as pd
# sales = pd.DataFrame({
#     "Order_ID": ["O101","O102","O103","O104"],
#     "Customer_ID": ["C01","C02","C01","C04"],
#     "Product_ID": ["P01","P02","P03","P01"],
#     "Quantity": [2,1,3,1],
#     "Revenue": [1200,800,2100,600]
# })
# customers = pd.DataFrame({
#     "Customer_ID": ["C01","C02","C03","C04"],
#     "Customer_Name": ["Arun","Priya","Rahul","Sneha"],
#     "City": ["Hyderabad","Chennai","Bengaluru","Hyderabad"],
#     "Segment": ["Retail","Corporate","Retail","Corporate"]
# })
# products = pd.DataFrame({
#     "Product_ID": ["P01","P02","P03"],
#     "Product": ["Laptop","Monitor","Phone"],
#     "Category": ["Electronics","Electronics","Mobile"]
# })
# print(sales)
# print(customers)
# print(products)

# # #concat
# jan = pd.DataFrame({
#     "Order_ID": ["O101","O102"],
#     "Revenue": [1200,800]
# })
# feb = pd.DataFrame({
#     "Order_ID": ["O103","O104"],
#     "Revenue": [2100,600]
# })
# combined = pd.concat([jan, feb],ignore_index=True
# )
# print(combined)

# # concat(axis=0) — Stack Rows
# result = pd.concat([jan, feb],axis=0,ignore_index=True
# )
# print(result)


# 5. concat(axis=1) — Combine by Index
# left = pd.DataFrame({"Customer":["A","B","C"]})
# right = pd.DataFrame({"Revenue":[1000,2000,1500]})
# result = pd.concat([left, right], axis=1)
# print(result)
# a = pd.DataFrame({"A":[10,20]}, index=[0,1])
# b = pd.DataFrame({"A":[30,40]}, index=[0,1])
# print(pd.concat([a,b], ignore_index=True))
# #concat with different columns
# a = pd.DataFrame({
#     "Order_ID":["O1","O2"],
#     "Revenue":[100,200]
# })
# b = pd.DataFrame({
#     "Order_ID":["O3"],
#     "City":["Hyderabad"]
# })
# print(pd.concat([a,b], ignore_index=True))


#    --- merge ---  
import pandas as pd
sales = pd.DataFrame({
    "Order_ID": [101,102,103,104,105],
    "Customer_ID": ["C001","C002","C003","C001","C005"],
    "Revenue": [500,700,400,300,900]
})
print(sales)
customers = pd.DataFrame({
    "Customer_ID": ["C001","C002","C003","C004"],
    "Customer_Name": ["Rahul","Priya","Arun","Sneha"],
    "City": ["Hyderabad","Bangalore","Chennai","Pune"],
    "Segment": ["Gold","Silver","Gold","Platinum"]
})
# print(customers)

# sales_customer=pd.merge(sales,customers,on="Customer_ID",how="right")
# sales_customer=pd.merge(sales,customers,on="Customer_ID",how="left")
# print(sales_customer)
# sales_customer=pd.merge(sales,customers,on="Customer_ID",how="inner")
# print(sales_customer)  #it removes nan rows
# sales_customer=pd.merge(sales,customers,on="Customer_ID",how="outer")
# print(sales_customer) #it fills from both tables 

# # 18. validate= — Protect the Relationship
# result = pd.merge( sales,customers,on="Customer_ID",how="left",validate="many_to_one")
# print(result)

# #many to many are dangerous becoz it prints  duplicate values alsoo 
# left = pd.DataFrame({"ID":["A","A"], "Value1":[10,20]})
# right = pd.DataFrame({"ID":["A","A"],"Value2":[100,200]})
# result = pd.merge(left, right, on="ID")
# print(result)


#day 9
import pandas as pd
sales = pd.DataFrame({
    "Order_ID": ["O101","O102","O103","O104","O105","O106"],
    "Month": ["Jan","Jan","Feb","Feb","Mar","Mar"],
    "City": ["Hyderabad","Chennai","Hyderabad","Bengaluru","Chennai","Hyderabad"],
    "Category": ["Electronics","Mobile","Electronics","Mobile","Electronics","Mobile"],
    "Product": ["Laptop","Phone","Monitor","Phone","Laptop","Phone"],
    "Quantity": [2,3,1,4,2,1],
    "Revenue": [120000,90000,25000,120000,130000,32000]
})

# 3. pivot()
# pivot() reshapes a DataFrame by placing unique values into row and column axes. It does not aggregate duplicate combinations. Therefore, every index + columns combination must identify one value.
result = sales.pivot(index="Month",columns="Category",values="Revenue")
print(result)

# pivot has a duplicate problem and it gives an error and it doesnt perform aggregate functions 
# pivot table () allows duplicate value and it can aggregate them 

# pivot table()
# import pandas as pd
# sales = pd.DataFrame({
# "Order_ID": ["O101", "O102", "O103", "O104", "O105"],
# "Month": ["Jan", "Jan", "Feb", "Feb", "Jan"],
# "City": ["Hyderabad", "Chennai", "Hyderabad", "Bengaluru", "Hyderabad"],
# "Category": ["Electronics", "Mobile", "Electronics", "Mobile", "Electronics"],
# "Product": ["Laptop", "Phone", "Monitor", "Phone", "Laptop"],
# "Quantity": [2, 3, 1, 4, 3],
# "Revenue": [120000, 90000, 25000, 120000, 180000]
# })
# print(sales)
# result=sales.pivot_table(index="Month",columns="Category",values="Revenue",aggfunc="sum")
# print(result) #it performs sum,max,min,count,mean

#margins=True IT calculates all rows and columns 
# result=sales.pivot_table(index="Month",columns="Category",values="Revenue",aggfunc="sum",margins=True)
# print(result)


# 1. melt()
# melt() converts wide data into long data. It is useful when repeated variables are stored as separate columns and need to become rows.

# wide = pd.DataFrame({
#     "Month": ["Jan","Feb","Mar"],
#     "Laptop": [120000,90000,130000],
#     "Phone": [80000,95000,110000],
#     "Monitor": [25000,30000,27000]
# })

# long = wide.melt(
#     id_vars="Month",
#     var_name="Product",
#     value_name="Revenue"
# )
# print(long)

# 28. stack()
# stack() moves a column level into the row index. It is particularly useful with MultiIndex columns.
# table = sales.pivot_table(
#     index="Month",
#     columns="Category",
#     values="Revenue",
#     aggfunc="sum"
# )

# stacked = table.stack()
# print(stacked)

