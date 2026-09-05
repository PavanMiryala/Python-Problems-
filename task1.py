import pandas as pd
# import numpy as np
data=pd.read_csv("C:/Users/pavan/OneDrive/Documents/Desktop/Pandas_Consolidation_Ecommerce_Sales.csv")
# data=pd.read_csv("./report1.csv")
# print(data)
# Display head(), tail(), shape, columns, info(), and describe().
# print(data.head())
# print(data.tail())
# print(data.shape)
# print(data.columns)
# print(data.info())
# print(data.describe())

# print(data.dtypes)
# numeric_cols=data.select_dtypes(include=["number"]).columns
# print(numeric_cols)
# categorical_columns=data.select_dtypes(include=["object"]).columns
# print(categorical_columns)
# print(data.isna())       #it shows the column values false if it not present then it show True 
# print(data.isna().sum()) #it shows missing values in columns that counts for whole column and display 
 
 #type conversion 
# data["Product"]=pd.to_numeric(data["Product"],errors="coerce")
# print(data["Product"].dtypes)
# print(data.dtypes)

#Task 2 column selection and indexing 
# Select Customer_Name.
# print(data["Customer_Name"])

# Select Product, Quantity, and Price.
# print(data[["Product","Quantity","Price"]]

# Select first 10 rows.
# print(data.head(10))

# Select rows 10–20.
# print(data.iloc[10:21])

# # Select Customer_Name and City for Completed orders.
# completedorders=data[data["Order_Status"]=="Completed"]
# print(completedorders[["Customer_Name","City"]])

# Set Order_ID as the index and reset it.
# data=data.set_index("Order_ID")
# print(data)


# Data Type Conversion
# Convert Order_Date to datetime.


# Convert Quantity, Price, and Discount to numeric.

# Verify with dtypes.

# Explain why incorrect types affect analysis.





