
data["Order_Date"] = pd.to_datetime(
    data["Order_Date"],
    format="%Y-%m-%d"
)
print(data["Order_Date"].dtype)