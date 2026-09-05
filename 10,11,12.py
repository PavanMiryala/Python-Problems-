import pandas as pd
dates = pd.to_datetime([
    "2026-01-05",
    "2026-02-15",
    "2026-03-20"
])
# print(dates)
# df = pd.DataFrame({
#     "Order_Date": ["2025-01-10", "2025-02-15", "2025-03-20"]
# })
# print(df)

import pandas as pd
df = pd.DataFrame({
    "Date": ["01-09-2026", "15-12-2025", "28-02-2024"]
})
# df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
# df["Date"] = pd.to_datetime(
#     df["Date"],
#     errors="coerce"
# )
# df[df["Date"].isna()]
# print(df)
# print(df["Date"].dtype)

# df["Year"] = df["Order_Date"].dt.year
# df["Month"] = df["Order_Date"].dt.month
# df["Day"] = df["Order_Date"].dt.day
# df["Quarter"] = df["Order_Date"].dt.quarter


date = pd.Timestamp("2026-08-27 10:30:00")

# print(date)

duration = pd.Timedelta(days=5)
new_date = pd.Timestamp("2026-08-27") + duration
print(duration)
print(new_date)