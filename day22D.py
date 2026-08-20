#dataframe is a 2d labeled data structure in pandas.it is similar to a table:rows represents records,columns represents variables ,and an index indentifies rows.

#creating a dataframe 
# import pandas as pd
# df=pd.DataFrame({
#     "name":["pavan","sai","vijay","akki","nikki","bunny","sunny"],
#     "marks":[30,30,45,24,30,43,21]
# })
# print(df)

#list of dictionary
# data = [
#     {"Name": "Rahul", "Age": 25, "Salary": 45000},
#     {"Name": "Priya", "Age": 28, "Salary": 60000},
#     {"Name": "Arun", "Age": 24, "Salary": 40000,"surname":"p"}
# ]
# df =pd.DataFrame(data)
# print(df)


#we can create by using numpy also
# import numpy as np
# arr=np.array([[101,2,1000],
#               [102,3,2000],
#               [103,4,30000]])
# df=pd.DataFrame(arr,
#                 columns=["empid","age","salary"])
# print(df)

#from series also we can add table
# names=pd.Series(["pavan","akki","anil"])
# ages=pd.Series([12,12,13])
# salaries=pd.Series([20000,30000,34000])
# df=pd.DataFrame({
#     "names":names,
#     "ages":ages,
#     "salaries":salaries})
# print(df)


# employees = pd.DataFrame({
#     "Employee_ID": ["E101", "E102", "E103", "E104", "E105", "E106"],
#     "Name": ["Rahul", "Priya", "Arun", "Meena", "Kiran", "Sneha"],
#     "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
#     "Age": [25, 29, 24, 32, 27, 31],
#     "Salary": [45000, 55000, 48000, 70000, 62000, 75000]
# })
# print(employees)

import pandas as pd
df = pd.read_csv("./data.csv")
print(df)