import pandas as pd

# 1. Loading the file (all sheets) 
file_path = "/content/Zepto_Dataset.xlsx"          
all_sheets = pd.read_excel(file_path, sheet_name=None)

print("Sheets found:", list(all_sheets.keys()))
for name, df in all_sheets.items():
    print(f"  {name}: {df.shape}")

# Checking the number of sheets and their shapes
for name, df in all_sheets.items():
    print(f"Sheet: {name} → {df.shape}")

file_path = "/content/Zepto_Dataset.xlsx"
all_sheets = pd.read_excel(file_path, sheet_name=None)

# Load each sheet individually
customers    = all_sheets['Customers']       
products     = all_sheets['Products']        
orders       = all_sheets['Orders']          
transactions = all_sheets['Transactions']    
ratings      = all_sheets['Ratings']         
delivery     = all_sheets['Delivery']        

# Step 1: Customers + Orders (join on C_ID)
df_updated = customers.merge(orders, on='C_ID', how='left')
# Step 2: + Products (join on P_ID)
df_updated = df_updated.merge(products, on='P_ID', how='left')
# Step 3: + Transactions (join on Or_ID)
df_updated = df_updated.merge(transactions, on='Or_ID', how='left')
# Step 4: + Ratings (need to check key — printing first)
print("Ratings columns:  ", ratings.columns.tolist())
print("Delivery columns: ", delivery.columns.tolist())

df_updated = customers \
    .merge(orders,       on='C_ID',  how='left') \
    .merge(products,     on='P_ID',  how='left') \
    .merge(transactions, on='Or_ID', how='left') \
    .merge(ratings,      on='Or_ID', how='left') \
    .merge(delivery,     on='DP_ID', how='left')

print(f"Final shape: {df_updated.shape}")
print(f"Columns: {df_updated.columns.tolist()}")

df_updated = df_updated.drop(columns=[col for col in df.columns if 'Unnamed' in col])
# Check which sheet is causing the fan-out
print("Orders Or_ID duplicates:      ", orders['Or_ID'].duplicated().sum())
print("Transactions Or_ID duplicates:", transactions['Or_ID'].duplicated().sum())
print("Ratings Or_ID duplicates:     ", ratings['Or_ID'].duplicated().sum())

#Deleting all duplicates entries
print(transactions[transactions['Or_ID'].duplicated(keep=False)].sort_values('Or_ID').head(10))
print(transactions['Transaction_Status'].value_counts())

#Based on Transactions only "Success"s are kept
transactions_clean = (
    transactions
    .sort_values('Transaction_Status', ascending=False)
    .drop_duplicates(subset='Or_ID', keep='first')
)

ratings_clean = ratings.drop_duplicates(subset='Or_ID', keep='first')

df_updated = customers \
    .merge(orders,             on='C_ID',  how='left') \
    .merge(products,           on='P_ID',  how='left') \
    .merge(transactions_clean, on='Or_ID', how='left') \
    .merge(ratings_clean,      on='Or_ID', how='left') \
    .merge(delivery,           on='DP_ID', how='left')
#Deleting all NAN values
df_updated = df_updated.drop(columns=[col for col in df.columns if 'Unnamed' in col])

print(f"Final shape: {df_updated.shape}")

print("Unique Or_IDs in orders:", orders['Or_ID'].nunique())
print("Unique C_IDs in orders: ", orders['C_ID'].nunique())
df_updated = orders \
    .merge(customers,          on='C_ID',  how='left') \
    .merge(products,           on='P_ID',  how='left') \
    .merge(transactions_clean, on='Or_ID', how='left') \
    .merge(ratings_clean,      on='Or_ID', how='left') \
    .merge(delivery,           on='DP_ID', how='left')

df_updated = df_updated.drop(columns=[col for col in df_updated.columns if 'Unnamed' in col])

print(f"Final shape: {df_updated.shape}")
df_updated.head()

df_updated.to_excel("Final_Dataset.xlsx", index=False)

#Standardization the data formats
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(0)
    else:
        df[col] = df[col].fillna('Unknown')

# Checking of Outliers
numeric_cols = df_updated.select_dtypes(include=['float64', 'int64']).columns.tolist()
print("Numeric columns:", numeric_cols)

# Stats to spot outliers visually
df_updated[numeric_cols].describe()

import matplotlib.pyplot as plt
fig, axes = plt.subplots(len(numeric_cols), 1, figsize=(10, 4 * len(numeric_cols)))
for i, col in enumerate(numeric_cols):
    axes[i].boxplot(df_updated[col], vert=False)
    axes[i].set_title(f'Boxplot - {col}')

plt.tight_layout()
plt.show()

df_updated_clean = df_updated.copy()
for col in numeric_cols:
    Q1 = df_updated_clean[col].quantile(0.25)
    Q3 = df_updated_clean[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    before = len(df_updated_clean)
    df_updated_clean = df_updated_clean[(df_updated_clean[col] >= lower) & (df_updated_clean[col] <= upper)]
    after = len(df_updated_clean)

    if before != after:
        print(f"{col}: removed {before - after} outlier rows")

print(f"\nBefore: {df_updated.shape[0]} rows")
print(f"After:  {df_updated_clean.shape[0]} rows")