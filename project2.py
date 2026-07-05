import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# LOAD DATASET
# ============================================

df = pd.read_excel("Cleaned_Dataset.xlsx")

print("=" * 60)
print("DECODELABS PROJECT 2 - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ============================================
# BASIC INFORMATION
# ============================================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# ============================================
# DESCRIPTIVE STATISTICS
# ============================================

print("\nDescriptive Statistics")
print(df.describe())

# ============================================
# PRODUCT ANALYSIS
# ============================================

print("\nProducts Sold")
print(df["Product"].value_counts())

# ============================================
# PAYMENT METHODS
# ============================================

print("\nPayment Methods")
print(df["PaymentMethod"].value_counts())

# ============================================
# ORDER STATUS
# ============================================

print("\nOrder Status")
print(df["OrderStatus"].value_counts())

# ============================================
# REFERRAL SOURCE
# ============================================

print("\nReferral Source")
print(df["ReferralSource"].value_counts())

# ============================================
# TOTAL PRICE ANALYSIS
# ============================================

print("\nAverage Total Price")
print(df["TotalPrice"].mean())

print("\nMaximum Total Price")
print(df["TotalPrice"].max())

print("\nMinimum Total Price")
print(df["TotalPrice"].min())

# ============================================
# QUANTITY ANALYSIS
# ============================================

print("\nAverage Quantity")
print(df["Quantity"].mean())

print("\nMaximum Quantity")
print(df["Quantity"].max())

print("\nMinimum Quantity")
print(df["Quantity"].min())

# ============================================
# TOP 10 PRODUCTS
# ============================================

top_products = df["Product"].value_counts()

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Products Sold")
plt.xlabel("Product")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("products_bar_chart.png")
plt.show()

# ============================================
# PAYMENT METHOD PIE CHART
# ============================================

payment = df["PaymentMethod"].value_counts()

plt.figure(figsize=(7,7))
payment.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig("payment_pie_chart.png")
plt.show()

# ============================================
# TOTAL PRICE HISTOGRAM
# ============================================

plt.figure(figsize=(8,5))
plt.hist(df["TotalPrice"], bins=20)
plt.title("Total Price Distribution")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("totalprice_histogram.png")
plt.show()

# ============================================
# QUANTITY BOXPLOT
# ============================================

plt.figure(figsize=(5,6))
plt.boxplot(df["Quantity"])
plt.title("Quantity Boxplot")
plt.tight_layout()
plt.savefig("quantity_boxplot.png")
plt.show()

# ============================================
# TOTAL PRICE BOXPLOT
# ============================================

plt.figure(figsize=(5,6))
plt.boxplot(df["TotalPrice"])
plt.title("Total Price Boxplot")
plt.tight_layout()
plt.savefig("totalprice_boxplot.png")
plt.show()

# ============================================
# MONTHLY TREND
# ============================================

df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["TotalPrice"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# ============================================
# REPORT
# ============================================

print("\n" + "=" * 60)
print("EDA REPORT")
print("=" * 60)

print(f"Total Orders: {len(df)}")
print(f"Unique Customers: {df['CustomerID'].nunique()}")
print(f"Unique Products: {df['Product'].nunique()}")

print(f"\nAverage Order Value: {df['TotalPrice'].mean():.2f}")
print(f"Highest Order Value: {df['TotalPrice'].max():.2f}")
print(f"Lowest Order Value: {df['TotalPrice'].min():.2f}")

print("\nMost Sold Product:")
print(df["Product"].value_counts().idxmax())

print("\nMost Used Payment Method:")
print(df["PaymentMethod"].value_counts().idxmax())

print("\nMost Common Order Status:")
print(df["OrderStatus"].value_counts().idxmax())

print("\nMost Common Referral Source:")
print(df["ReferralSource"].value_counts().idxmax())

print("=" * 60)
print("PROJECT 2 COMPLETED SUCCESSFULLY")
print("=" * 60)