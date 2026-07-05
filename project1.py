import pandas as pd
# STEP 1-Load the dataset
file_name = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(file_name)
print("=" * 50)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)
# STEP 2-Basic Information
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())
# STEP 3-Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

if "ReferralSource" in df.columns:
    df["ReferralSource"] = df["ReferralSource"].fillna("Unknown")
# STEP 4-Duplicate Rows
duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows Before Cleaning: {duplicates}")

df = df.drop_duplicates()

print(f"Duplicate Rows After Cleaning: {df.duplicated().sum()}")
# STEP 5-Duplicate Order IDs
duplicate_orders = df["OrderID"].duplicated().sum()

print(f"\nDuplicate Order IDs: {duplicate_orders}")
# STEP 6-Date Formatting

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
# STEP 7-Clean Text Columns
text_columns = [
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "TrackingNumber",
    "CouponCode",
    "ReferralSource"
]

for column in text_columns:
    if column in df.columns:
        df[column] = df[column].astype(str).str.strip()

# STEP 8-Check Data Types

print("\nData Types:")
print(df.dtypes)
# STEP 9-Final Quality Check

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nRemaining Duplicate Rows:")
print(df.duplicated().sum())
# STEP 10 - Save Clean Dataset
output_file = "Cleaned_Dataset.xlsx"

df.to_excel(output_file, index=False)

print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY")
print(f"Clean dataset saved as: {output_file}")
print("=" * 50)