#TASK 1
# import pandas as pd
# marks = pd.Series([78, 92, 65, 88, 74, 95],
#     index=["S101", "S102", "S103", "S104", "S105", "S106"],
#     name="Marks"
# )

# print(marks)
# print(marks.index)
# print(marks.values)
# print(marks.dtype)
# print(marks.shape)
# print(marks.size)
# print(marks.ndim)
# print(marks.name)
# print(marks.mean())
# print(marks.max())
#print(marks.idxmax())
#print(marks[marks>80])
#print(marks.iloc[:3])
# print(marks.loc["S104"])

# #TASK 2
# import pandas as pd
# prices=pd.Series([1200, 850, 2300, 1750, 950, 3200],
#                 index=["P101", "P102", "P103", "P104", "P105", "P106"],
#                 name="Price")
# print(prices)
# print(prices.sum())
# print(prices.mean())
# print(prices.min())
# print(prices.max())
# print(prices.idxmax())
# print(prices[prices>1500])
# print(prices[(prices>1000) & (prices<2500)])
# prices=prices*1.10
# print(prices)
# print(prices.nlargest(3))


# #TASK 3
# import pandas as pd
# employees = pd.DataFrame({
#         "EmpID": ["E101", "E102", "E103", "E104", "E105"],
#     "Name": ["Rahul", "Priya", "Arun", "Meena", "Kiran"],
#     "Age": [25, 29, 24, 32, 27],
#     "Department": ["IT", "HR", "IT", "Sales", "Finance"],
#     "Salary": [45000, 55000, 48000, 70000, 85000]

# })
# print(employees)
# print(employees.shape)
# print(employees.size)
# print(employees.ndim)
# print(employees.index)
# print(employees.columns)
# print(employees.values)
# print(employees.dtypes)

# print(employees["Name"])
# print(employees[["Name","Salary"]])
# print(employees.iloc[:3])
# print(employees.iloc[-2:])
# print(employees.iloc[2])
# print(employees.iloc[2, 4])

# TASK 4 EMPLOYEE FILTERING

# import pandas as pd
# employees = pd.DataFrame({
#         "EmpID": ["E101", "E102", "E103", "E104", "E105"],
#     "Name": ["Rahul", "Priya", "Arun", "Meena", "Kiran"],
#     "Age": [25, 29, 24, 32, 27],
#     "Department": ["IT", "HR", "IT", "Sales", "Finance"],
#     "Salary": [45000, 55000, 48000, 70000, 85000]

# })
# print(employees[employees["Department"]=="IT"])
# print(employees[employees["Department"]=="HR"])
# print(employees[employees["Salary"]>50000])

# print(employees[employees["Salary"]<50000])
# print(employees[employees["Age"]>27])
# print(employees[employees["Age"]<25])
# print(employees[(employees["Salary"] > 50000) & (employees["Age"] > 27)])

# print(employees[(employees["Department"]=="IT") | (employees["Department"]=="HR")])
# print(employees[(employees["Salary"] >= 45000) & (employees["Salary"] <= 75000)])
# print(employees[~(employees["Salary"] > 50000)])

#TASK 5
import pandas as pd

employees = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Arun", "Meena"],
    "Department": ["IT", "HR", "IT", "Sales"],
    "Salary": [45000, 55000, 48000, 70000]
}, index=["E101", "E102", "E103", "E104"])
# print(employees.loc["E101"])
# print(employees.loc["E103"])
# print(employees.loc["E102",["Name","Salary"]])
# print(employees.loc["E101":"E103"])
# print(employees.iloc[0])
# print(employees.iloc[3, 2])
# print(employees.iloc[:3])
# print(employees.iloc[:, [0, 2]])
