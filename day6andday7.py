#MISSING DATA AND DATA CLEANING 
import pandas as pd
import numpy as np
data=pd.read_csv("./report.csv")
print(data)
messy = data.copy()
# messy.loc[2, "Price"] = np.nan
# messy.loc[5, "City"] = np.nan
# messy.loc[8, "Quantity"] = np.nan
# messy.loc[12, "Category"] = np.nan
# messy.loc[17, "Order_Date"] = pd.NaT
# print(messy.head(20))
# print("\n6. Missing Values using isna()")
# print(messy.isna())
# Check only one column
# print("\nPrice Missing?")
# print(messy["Price"].isna())
# # 7. isnull() - Same as isna()
# print("\n7. Missing Values using isnull()")
# print(messy["City"].isnull())
# # 8. Count Missing Values
# print(messy.isna().sum())

# # 9. Missing Percentage
# missing_percentage = messy.isna().mean() * 100
# print(missing_percentage)

# # 10. Total Missing Cells
# total_missing = messy.isna().sum().sum()
# print(total_missing)

# 11. Rows Having Any Missing Value
# rows_with_missing = messy[messy.isna().any(axis=1)]
# print(rows_with_missing)
# # 12. Completely Blank Rows
# blank_rows = messy[messy.isna().all(axis=1)]
# print(blank_rows)
# # 13. axis=0 vs axis=1
# print("\n13A. Missing Count Column Wise (axis=0)")
# print(messy.isna().sum(axis=0))

# print("\n13B. Missing Count Row Wise (axis=1)")
# print(messy.isna().sum(axis=1))

# print("\n13C. Any Missing in Row")
# print(messy.isna().any(axis=1))

# print("\n13D. All Missing in Row")
# print(messy.isna().all(axis=1))

# # 14. dropna() - Remove Missing Rows
# print("\n14. dropna()")
# drop_all_missing_rows = messy.dropna()
# print(drop_all_missing_rows)
# print("Shape After dropna():", drop_all_missing_rows.shape)

# # 15. dropna(how='any')

# print("\n15. dropna(how='any')")
# print(messy.dropna(how="any"))

# # 16. dropna(how='all')

# print("\n16. dropna(how='all')")
# print(messy.dropna(how="all"))
# # 17. dropna(subset=[])
# revenue_data = messy.dropna(
#     subset=["Quantity", "Price"]
# )

# print(revenue_data)
# # 18. dropna(thresh=)
# threshold_data = messy.dropna(thresh=6)
# print(threshold_data)
# # 19. fillna() - Replace Missing Values
# filled_city = messy.copy()
# filled_city["City"] = filled_city["City"].fillna("Unknown")
# print(filled_city[["City"]].head(20))

# # 20. fillna(0)
# price_zero = messy.copy()
# price_zero["Price"] = price_zero["Price"].fillna(0)
# print(price_zero[["Price"]].head(20))

# # 21. Mean Imputation
# mean_price = messy["Price"].mean()
# mean_fill = messy.copy()
# mean_fill["Price"] = mean_fill["Price"].fillna(mean_price)
# print("Mean Price :", mean_price)
# print(mean_fill[["Price"]].head(20))
# # 22. Median Imputation
# median_price = messy["Price"].median()
# median_fill = messy.copy()
# median_fill["Price"] = median_fill["Price"].fillna(median_price)
# print("Median Price :", median_price)
# print(median_fill[["Price"]].head(20))

# # 23. Mode Imputation
# mode_city = messy["City"].mode()[0]
# mode_fill = messy.copy()
# mode_fill["City"] = mode_fill["City"].fillna(mode_city)
# print("Most Common City :", mode_city)
# print(mode_fill[["City"]].head(20))
# # 24. Different Columns Different Fill Strategys
# multi_fill = messy.copy()
# multi_fill = multi_fill.fillna({
#     "City": "Unknown",
#     "Category": "Unknown",
#     "Price": multi_fill["Price"].median()
# })

# print(multi_fill.head(20))

# # 25. Forward Fill (ffill)
# series = pd.Series([
#     "A", None, None, "B", None
# ])
# print("Original Series")
# print(series)

# print("\nAfter Forward Fill")
# print(series.ffill())
# # 26. Backward Fill (bfill)
# print(series.bfill())

# # ==========================================================
# # 27. Missing Values in Arithmetic
# # ==========================================================

# print("\n27. Arithmetic with Missing Values")

# numbers = pd.Series([100, 200, np.nan, 400])

# print("Original")
# print(numbers)

# print("\nMultiply by 2")
# print(numbers * 2)

# print("\nMean")
# print(numbers.mean())

# # ==========================================================
# # 28. skipna=True vs skipna=False
# # ==========================================================

# print("\n28. skipna Comparison")

# print("Mean (skipna=True)")
# print(numbers.mean(skipna=True))

# print("Mean (skipna=False)")
# print(numbers.mean(skipna=False))

# # ==========================================================
# # 29. Revenue Calculation
# # ==========================================================

# print("\n29. Revenue Calculation")

# revenue = messy.copy()

# revenue["Revenue"] = (
#     revenue["Quantity"] * revenue["Price"]
# )

# print(revenue[
#     ["Order_ID", "Quantity", "Price", "Revenue"]
# ])

# # ==========================================================
# # 30. Orders Having Missing Revenue
# # ==========================================================

# print("\n30. Orders with Missing Revenue")

# missing_revenue = revenue[
#     revenue["Revenue"].isna()
# ]

# print(missing_revenue[
#     ["Order_ID", "Quantity", "Price", "Revenue"]
# ])

# # ==========================================================
# # 31. Before vs After Cleaning
# # ==========================================================

# print("\n31. Before vs After Cleaning")

# before = messy.isna().sum()

# cleaned = messy.copy()

# cleaned["City"] = cleaned["City"].fillna("Unknown")
# cleaned["Category"] = cleaned["Category"].fillna("Unknown")
# cleaned["Price"] = cleaned["Price"].fillna(
#     cleaned["Price"].median()
# )

# after = cleaned.isna().sum()

# print("\nBefore Cleaning")
# print(before)

# print("\nAfter Cleaning")
# print(after)

# # ==========================================================
# # 32. Final Revenue After Cleaning
# # ==========================================================

# print("\n32. Revenue After Cleaning")

# cleaned["Revenue"] = (
#     cleaned["Quantity"] * cleaned["Price"]
# )

# print(cleaned[
#     ["Order_ID", "Quantity", "Price", "Revenue"]
# ])

# # ==========================================================
# # 33. High Value Orders (>50000)
# # ==========================================================

# print("\n33. High Value Orders")

# cleaned["High_Value"] = (
#     cleaned["Revenue"] > 50000
# )

# print(cleaned[
#     ["Order_ID", "Revenue", "High_Value"]
# ])

# # ==========================================================
# # 34. Sort Revenue Highest to Lowest
# # ==========================================================

# print("\n34. Sort Revenue Descending")

# sorted_revenue = cleaned.sort_values(
#     by="Revenue",
#     ascending=False
# )

# print(sorted_revenue[
#     ["Order_ID", "Revenue"]
# ])

# # ==========================================================
# # 35. Export Cleaned Dataset
# # ==========================================================

# print("\n35. Export Cleaned Dataset")

# cleaned.to_csv(
#     "cleaned_sales_day6.csv",
#     index=False
# )

# print("File Saved : cleaned_sales_day6.csv")

# # ==========================================================
# # 36. Reload Exported File
# # ==========================================================

# print("\n36. Reload Cleaned Dataset")

# final_data = pd.read_csv("cleaned_sales_day6.csv")

# print(final_data.head())

# # ==========================================================
# # 37. Final Missing Data Audit
# # ==========================================================

# print("\n37. Final Missing Count")

# print(final_data.isna().sum())

# print("\nFinal Missing Percentage")

# print(final_data.isna().mean() * 100)

# print("\nDataset Shape")
# print(final_data.shape)

# print("\nData Cleaning Completed Successfully!")
# print("=" * 60)



#day 77777
import pandas as pd
import numpy as np
data = pd.read_csv("./report.csv")
# print(data)
messy = data.copy()
# messy = pd.concat([messy, messy.iloc[[2, 5, 8]]], ignore_index=True)
# print(messy)
# print(messy.duplicated())

# duplicate_count = messy.duplicated().sum()
# print(duplicate_count)

# duplicates = messy[messy.duplicated()]
# print(duplicates)

# print(messy.duplicated(keep="first"))
# print(messy.duplicated(keep="last"))
# print(messy.duplicated(keep=False))

# clean_duplicate = messy.drop_duplicates()
# print(clean_duplicate)

# print(messy.duplicated(subset=["Order_ID"]))

# unique_orders = messy.drop_duplicates(subset=["Order_ID"])
# print(unique_orders)

# latest_orders = messy.sort_values("Order_Date").drop_duplicates(
#     subset=["Order_ID"],
#     keep="last"
# )
# print(latest_orders)

# print(messy.duplicated(subset=["Order_ID", "Customer_ID"]))

# print(messy["City"].value_counts(dropna=False))
# print(messy["Category"].value_counts(dropna=False))

# messy.loc[0, "City"] = " Hyderabad "
# messy.loc[1, "City"] = "HYDERABAD"
# messy.loc[2, "City"] = "hyderabad"

# messy.loc[3, "Category"] = " electronics "
# messy.loc[4, "Category"] = "ELECTRONICS"

# print(messy[["City", "Category"]].head())

# strip_city = messy.copy()
# strip_city["City"] = strip_city["City"].astype("string").str.strip()
# print(strip_city["City"].head())

# lower_city = messy.copy()
# lower_city["City"] = lower_city["City"].astype("string").str.lower()
# print(lower_city["City"].head())

# upper_city = messy.copy()
# upper_city["City"] = upper_city["City"].astype("string").str.upper()
# print(upper_city["City"].head())

# title_city = messy.copy()
# title_city["City"] = title_city["City"].astype("string").str.title()
# print(title_city["City"].head())

# replace_city = messy.copy()
# replace_city["City"] = replace_city["City"].astype("string").str.replace(
#     "Hyd.", "Hyderabad", regex=False
# )
# print(replace_city["City"].head())

# salary = pd.Series(["₹62,000", "₹45,500", "₹18,750"])

# clean_salary = (
#     salary.str.replace("₹", "", regex=False)
#           .str.replace(",", "", regex=False)
# )

# print(clean_salary)
# print(pd.to_numeric(clean_salary))

# messy["Product_Length"] = messy["Product"].astype("string").str.len()
# print(messy[["Product", "Product_Length"]].head())

# contains_phone = messy[
#     messy["Product"].astype("string").str.contains(
#         "phone",
#         case=False,
#         na=False
#     )
# ]
# print(contains_phone)

# starts_A = messy[
#     messy["Product"].astype("string").str.startswith(
#         "A",
#         na=False
#     )
# ]
# print(starts_A)

# ends_pro = messy[
#     messy["Product"].astype("string").str.endswith(
#         "Pro",
#         na=False
#     )
# ]
# print(ends_pro)

# names = pd.Series([
#     "Mani Jakka",
#     "Rahul Kumar",
#     "Priya Reddy"
# ])

# split_names = names.str.split(" ", expand=True)
# print(split_names)

# order_numbers = messy["Order_ID"].astype("string").str.extract(r"(\d+)")
# print(order_numbers.head())

# products = pd.Series([
#     "Phone   - 128GB",
#     "Phone    - 256GB",
#     "Phone      - 512GB"
# ])

# clean_products = products.str.replace(
#     r"\s+",
#     " ",
#     regex=True
# )
# print(clean_products)

# city_clean = messy.copy()

# city_clean["City"] = (
#     city_clean["City"]
#     .astype("string")
#     .str.strip()
#     .str.title()
# )

# print(city_clean["City"].value_counts())

# category_clean = messy.copy()

# category_clean["Category"] = (
#     category_clean["Category"]
#     .astype("string")
#     .str.strip()
#     .str.title()
# )

# print(category_clean["Category"].value_counts())

# city_map = {
#     "Hyd": "Hyderabad",
#     "Hyd.": "Hyderabad",
#     "Secbad": "Secunderabad"
# }

# mapped = messy.copy()
# mapped["City"] = mapped["City"].replace(city_map)
# print(mapped["City"].head())

# before = messy.copy()
# before["Revenue"] = before["Quantity"] * before["Price"]

# print(before.groupby("City")["Revenue"].sum())

# after = messy.copy()

# after["City"] = (
#     after["City"]
#     .astype("string")
#     .str.strip()
#     .str.title()
# )

# after["Revenue"] = after["Quantity"] * after["Price"]

# print(after.groupby("City")["Revenue"].sum())

# duplicate_check = after.duplicated(
#     subset=["Order_ID", "City"],
#     keep=False
# )

# print(after[duplicate_check])

# final = data.copy()

# for col in ["Product", "Category", "City"]:
#     final[col] = (
#         final[col]
#         .astype("string")
#         .str.strip()
#     )

# final["Category"] = final["Category"].str.title()
# final["City"] = final["City"].str.title()

# print(final.duplicated().sum())
# print(final["Order_ID"].duplicated().sum())

# final = final.drop_duplicates()

# final["Quantity"] = pd.to_numeric(final["Quantity"], errors="coerce")
# final["Price"] = pd.to_numeric(final["Price"], errors="coerce")

# final["Revenue"] = final["Quantity"] * final["Price"]

# print(final.head())

# summary = {
#     "Total Rows": len(final),
#     "Duplicate Rows": final.duplicated().sum(),
#     "Missing Values": final.isna().sum().sum()
# }

# print(summary)

# final.to_csv("cleaned_sales_day7.csv", index=False)

# reload_data = pd.read_csv("cleaned_sales_day7.csv")

# print(reload_data.head())
# print(reload_data.isna().sum())
# print(reload_data.shape)