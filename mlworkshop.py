import pandas as pd
from sklearn.linear_model import LinearRegression
data={"exp":[1,2,3,4,5],
      "salary":[10000,15000,20000,25000,30000]}

df=pd.DataFrame(data)

#input output
x=df[["exp"]].values
y=df["salary"]
model=LinearRegression()
model.fit(x,y)

pred=model.predict([[6]])
print(pred)