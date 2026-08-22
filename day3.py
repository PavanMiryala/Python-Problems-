import pandas as pd
df=pd.DataFrame({
    "org_name":["google","oracle","infosys","jp morgan","deloitte"],
    "dept_name":["IT","HR","sales","marketing","managing"],
    "type":["product","product","service","service","service"],
    "salary":[30000,40000,50000,60000,70000]
},index=["c1","c2","c3","c4","c5"])
# print(df[df["type"]=="product"])

#isin

# print(df[df["dept_name"].isin(["IT","managing"])]) #instead of and & we can use this isin
# print(df[df["dept_name"].isin(["IT","managing"])]["org_name"])

#between () range
# print(df[df["salary"].between(40000,70000,inclusive="left")]) #here inclusive="left"  reomves the last value that is highest 
# print(df[df["salary"].between(40000,70000,inclusive="right")]) #here inclusive="left"  removes the lowest

# print(df[df["salary"].between(40000,70000,inclusive="neither")]) #here inclusive="neither" removes lowest and highest 

#query
# print(df.query("dept_name == 'IT'"))

#query wiht variable 
minimum_salary=60000
print(df.query(f"salary>{minimum_salary}"))