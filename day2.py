import pandas as pd
marks = pd.Series(
    [78, 92, 65, 88, 74, 95],
    index=["S101", "S102", "S103", "S104", "S105", "S106"],
    name="Marks"
)
print(marks)
print(marks.index)
print(marks.values)
print(marks.dtype)
print(marks.shape)
print(marks.size)
print(marks.ndim)
print(marks.name)

print(marks.mean())
print(marks.max())
print(marks.idxmax())
print(marks[marks > 80])
print(marks.iloc[:3])
print(marks.loc["S104"])
print((marks / marks.sum()) * 100)


prices = pd.Series(
    [1200, 850, 2300, 1750, 950, 3200],
    index=["P101", "P102", "P103", "P104", "P105", "P106"],
    name="Price"
)
print(prices)
print(prices.sum())
print(prices.mean())
print(prices.min())
print(prices.max())
print(prices.idxmax())

print(prices[prices > 1500])
print(prices[(prices >= 1000) & (prices <= 2500)])
prices = prices * 1.10
print(prices)

print(prices.nlargest(3))
import pandas as pd
s=pd.Series([1,2,3,4,5,6,7,8,9,9,10])
print(s.head()) #it returns the first few elements instead of searching all
print(s.tail()) # it returns the last few elements instead of searching all
print(s.sum())
print(s.median())
print(s.min())
print(s.std()) #it is the square root of variance 
print(s.unique()) #it removes duplicate values and print unique
print(s.nunique())# it describes total no.of uniques 
print(s.value_counts())#it counts the value how many rimes it has repaeated 
print(s.idxmax())
print(s.idxmin())
print(s.nlargest())#it gives few highest numbers
print(s.nsmallest())

