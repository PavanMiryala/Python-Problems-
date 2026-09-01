# import pandas as pd
# df=pd.DataFrame({
#     "org_name":["google","oracle","infosys","jp morgan","deloitte"],
#     "dept_name":["IT","HR","sales","marketing","managing"],
#     "type":["product","product","service","service","service"],
#     "salary":[30000,40000,50000,60000,70000]
# },index=["c1","c2","c3","c4","c5"])
# print(df[df["type"]=="product"])

# # isin

# print(df[df["dept_name"].isin(["IT","managing"])]) #instead of and & we can use this isin
# print(df[df["dept_name"].isin(["IT","managing"])]["org_name"])

# between () range
# print(df[df["salary"].between(40000,70000,inclusive="left")]) #here inclusive="left"  reomves the last value that is highest 
# print(df[df["salary"].between(40000,70000,inclusive="right")]) #here inclusive="right"  removes the lowest

# print(df[df["salary"].between(40000,70000,inclusive="neither")]) #here inclusive="neither" removes lowest and highest 

# # query
# print(df.query("dept_name == 'IT'"))

# # query wiht variable 
# minimum_salary=60000
# print(df.query(f"salary>{minimum_salary}"))

# import pandas as pd
# df=pd.DataFrame({
#     "org_name":["google","oracle","infosys","jp morgan","deloitte"],
#     "dept_name":["IT","HR","sales","marketing","managing"],
#     "type":["product","product","service","service","service"],
#     "salary":[30000,40000,50000,60000,70000]
# },index=["c1","c2","c3","c4","c5"])


#where 
# print(df.where(df["salary"]>50000,other="N/A")) #it prints true values 


# mask()
# print(df.mask(df["salary"]<50000)) #it hides true values it prints false values doest not print it gives nan


#IOC + BOOLEAN FILTERING
# print(df.loc[df["salary"]>50000,
#        ["org_name","type","salary"]])


#filter
# print(df.filter(like="sal"))# it matches the alphabets and gives that column 

#PRACTICING THE TASK WHICH I HAVE LEARNED TODAY
import pandas as pd

# employees = pd.DataFrame({
#     "empid": ["E101","E102","E103","E104","E105","E106","E107","E108"],
#     "name": ["Rahul","Priya","Arun","Meena","Kiran","Sneha","Vikram","Anjali"],
#     "department": ["IT","HR","IT","Sales","Finance","IT","HR","Finance"],
#     "city": ["Hyderabad","Mumbai","Hyderabad","Chennai","Delhi","Hyderabad","Mumbai","Bangalore"],
#     "age": [25,29,24,32,35,31,27,30],
#     "salary": [45000,55000,48000,70000,85000,75000,62000,68000],
#     "experience": [2,5,1,8,10,7,4,6]
# })

# print(employees)

# Solve using Boolean Filtering.
# 1.Select employees whose salary is greater than ₹50,000.

# print(employees[employees["salary"]>60000])
#now i got a doubt that i need to print less then condiitin values also by using other to use ohter we need where or mask 
# employees["salary"]=employees["salary"].where(employees["salary"]>60000,other="n/A")
# print(employees)

# 2.Select employees whose age is less than 30.
# print(employees[employees["age"]<30])

# 3.Select employees from the IT department.
# print(employees[employees["department"]=="IT"])

# 4.Select employees from Hyderabad.
# print(employees[employees["city"]=="Hyderabad"])

# 5.Select employees whose experience is more than 5 years.
# print(employees[employees["experience"]>5])

#6.Select employees whose salary is less than ₹60,000.
# print(employees[employees["salary"]<60000])

#7.Select employees whose age is exactly 30.
# print(employees[employees["age"]==30])

# 8.Select employees who are not from Mumbai.
# print(employees[employees["city"]!="Mumbai"])
# print(employees[employees["city"].ne("Mumbai")])

# 9. Select employees whose department is not Finance.
# print(employees[employees["department"].ne("Finance")])
# print(employees[employees["department"]!="Finance"])

# 10.Select employees earning ₹70,000 or more.
# print(employees[employees["salary"] >= 70000])
# print(employees[employees["salary"].ge(70000)])

# # NOW MULTIPLE CONDITIONS USING &,|  AND ~.
employees = pd.DataFrame({
    "empid": ["E101","E102","E103","E104","E105","E106","E107","E108"],
    "name": ["Rahul","Priya","Arun","Meena","Kiran","Sneha","Vikram","Anjali"],
    "department": ["IT","HR","IT","Sales","Finance","IT","HR","Finance"],
    "city": ["Hyderabad","Mumbai","Hyderabad","Chennai","Delhi","Hyderabad","Mumbai","Bangalore"],
    "age": [25,29,24,32,35,31,27,30],
    "salary": [45000,55000,48000,70000,85000,75000,62000,68000],
    "experience": [2,5,1,8,10,7,4,6]
})

# 11 Select IT employees whose salary is above ₹50,000
# print(employees[(employees["department"]=="IT")&
#                 (employees["salary"]>50000)])

# print(employees[(employees["department"]=="IT")&
#                  (employees["salary"].gt(50000))])

# Q12 Select employees from Hyderabad whose experience is greater than 3 years.
# print(employees[(employees["city"]=="Hyderabad") & (employees["experience"] > 3)])

# Q13 Select employees from HR or Finance.
# print(employees[(employees["department"]=="HR") | (employees["department"]=="Finance")])


# Q14. Select employees who are from IT or Sales.
# print(employees[(employees["department"]=="IT") | (employees["department"]=="Finance")])


# Q15 Select employees whose age is above 25 and salary below ₹80,000.
# print(employees[(employees["age"]>25) & (employees["salary"]<80000 )])

# Q16 Select employees who are not from IT and not from Hyderabad.
# print(employees[(employees["department"]!="IT") & (employees["city"]!="Hyderabad")])
# print(employees[~(employees["department"]=="IT") & ~(employees["city"]=="Hyderabad")])

# Q17 Select employees from Mumbai or Chennai with salary above ₹60,000.
# print(employees[(employees["city"]=="Mumbai")|(employees["city"]=="Chennai") & (employees["salary"]>60000)])

# Q18 Select employees whose experience is between 3 and 8 years and salary above ₹55,000.
# print(employees[(employees["experience"]>3) & (employees["experience"]<8) & (employees["salary"]>55000)])


# Level 3 – isin() and between()

#19 Select employees from IT, HR, or Finance using isin().
# print(employees[employees["department"].isin(["IT","HR","Finance"])])

# Q20 Select employees from Hyderabad or Bangalore using isin().
# print(employees["city"].isin(["Hyderabad","Bangalore"]))

# Q21 Select employees aged between 25 and 30 using between().
# print(employees[employees["age"].between(25,30)])
# print(employees[employees["age"].between(25, 30)])

# Q22 Select employees earning between ₹50,000 and ₹80,000 using between().
# print(employees[employees["salary"].between(50000,80000)])

# Q23 Select employees whose experience is between 2 and 6 years.
# print(employees[employees["experience"].between(2,6)])

# Q24 Select employees who are not from IT or HR using ~isin().
# print(employees[~employees["department"].isin(["IT", "HR"])])