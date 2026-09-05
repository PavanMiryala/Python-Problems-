# import pandas as pd 
# data=pd.read_csv("C:/Users/pavan/Downloads/Pandas_Day_4_Real_World_Sales_Data.csv")
# # data=pd.read_csv("./reprot.csv")
# print(data)
# print(data.shape)#to check the columns and rows
# print(data.dtypes) #to check the datatypes 
# print(data.describe()) #it performs calculations to all numeric values in the table like means,count,std,var,eetc
# print(type(data))

# print(data.sample()) #it prints random value and if we mention any number in that so it should give random rows accoording to the number 
# print(data.info()) #it summarizes all the column records and how much space and memory it is ocupaid it sboes  

# data=pd.read_excel("C:\\Users\\pavan\\OneDrive\\Documents\\Desktop\\Pandas_Day_4_Real_World_Sales_Data.csv.xlsx")
# print(data.info())

# # BUSINESS QUESTION
# # How many orders are present?
# print(data.shape[1])

# # select columns 
# print(data[["Order_ID", "Product", "Quantity", "Price"]])

# # to create a column 
# data["Revenue"]=data["Quantity"]*data["Price"]
# print(data)
# bulk_order=data["Quantity"]>10
# print(data[bulk_order])

# # to convert code too creating new file
# data.to_csv("./report.csv")

#DAY 5
# Data Types, Type Conversion & Validation
# ==========================================
import pandas as pd
# Load CSV File
data = pd.read_csv("./report.csv")
# # 1. Check Data Types
# print(data.dtypes)
# print(data["Price"].dtype)
# print(data["Order_Date"].dtype)
# # Check Python data types inside a column
# print(data["Order_Date"].map(type).value_counts())
# # 2. astype() - Direct Conversion
# data["Order_ID"] = data["Order_ID"].astype("string")
# data["Customer_ID"] = data["Customer_ID"].astype("string")
# data["Quantity"] = data["Quantity"].astype("int64")
# data["Price"] = data["Price"].astype("float64")
# print(data.dtypes)
# # 3. astype() Example
# values = pd.Series(["100", "200", "300"])
# numbers = values.astype("int64")
# print(numbers)
# print(numbers.dtype)
# # 4. pd.to_numeric()
# values = pd.Series(["100", "200", "300"])
# numbers = pd.to_numeric(values)
# print(numbers)
# print(numbers.dtype)
# # 5. pd.to_numeric(errors="coerce")   #it prints error values as nan
# values = pd.Series(["100", "200", "unknown", "400"])
# numbers = pd.to_numeric(values, errors="coerce")
# print(numbers)
# print(numbers.dtype)

# # 6. Convert Quantity and Price Safely
# data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
# data["Price"] = pd.to_numeric(data["Price"], errors="coerce")
# print(data.dtypes)

# # # 7. Convert Date Column
# data["Order_Date"] = pd.to_datetime(
#     data["Order_Date"],
#     format="%Y-%m-%d"
# )
# print(data["Order_Date"].dtype)

# # Datetime Components
# data["Order_Year"] = data["Order_Date"].dt.year
# data["Order_Month"] = data["Order_Date"].dt.month
# data["Order_Day"] = data["Order_Date"].dt.day
# data["Order_Quarter"] = data["Order_Date"].dt.quarter

# print(
#     data[[
#         "Order_Date",
#         "Order_Year",
#         "Order_Month",
#         "Order_Day",
#         "Order_Quarter"
#     ]]
# )

# 10. Create Revenue Column
data["Revenue"] = data["Quantity"] * data["Price"]
print(data[["Quantity", "Price", "Revenue"]])

# 11. Boolean Data Type
data["High_Value"] = data["Revenue"] > 50000
print(data[["Revenue", "High_Value"]])
print(data["High_Value"].dtype)

# 12. Category Data Type
data["Category"] = data["Category"].astype("category")
data["City"] = data["City"].astype("category")
print(data.dtypes)
# 13. Category Information

print(data["Category"].cat.categories)
print(data["Category"].cat.codes)

# 14. Memory Usage
print(data.memory_usage(deep=True))
print(data.memory_usage(deep=True).sum())

# 15. Type Validation
from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_bool_dtype
)
print(is_numeric_dtype(data["Price"]))
print(is_datetime64_any_dtype(data["Order_Date"]))
print(is_bool_dtype(data["High_Value"]))

# 16. Date Filtering
august_orders = data[
    data["Order_Date"] >= "2026-08-01"
]
print(august_orders)

print(data.head())