#Task 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import warnings
warnings.filterwarnings('ignore')

PALETTE = ["#4C72B0","#55A868","#DD8452","#C44E52","#8172B2",
           "#64B5CD","#937860","#DA8BC3","#8C8C8C","#CCB974",
           "#4C9B5E","#E05A4E","#7B9EC8","#F0A500","#9E6B8A"]
BLUE,GREEN,ORANGE,RED,PURPLE,TEAL = PALETTE[:6]

plt.rcParams.update({
    "figure.facecolor":"white","axes.facecolor":"#F5F5F5",
    "axes.edgecolor":"#CCCCCC","axes.grid":True,
    "grid.color":"white","grid.linewidth":0.9,
    "font.size":10,"axes.titlesize":12,"axes.titleweight":"bold",
    "axes.labelsize":10,"xtick.labelsize":9,"ytick.labelsize":9,
})

def save(fig, name):
    path = f"/content/Updated_Zepto_Dataset.xlsx{name}"
    fig.savefig(path, dpi=150, bbox_inches='tight')
    print(f"  Saved -> {path}")
    plt.close(fig)

# Load
df_updated = pd.read_excel('/content/Updated_Zepto_Dataset.xlsx')
df_updated['Order_Amount'] = df_updated['Price'] * df_updated['Qty'] * (1 - df_updated['Coupon_Discount'] / 100)

num_cols = ['Age','Qty','Price','Coupon_Discount','Order_Amount','Prod_Rating','Delivery/Service_Rating']
cat_cols = ['gender','Category','Brand','Transaction_Mode','Transaction_Status','City','State','Delivery Partner']

print(f"Dataset: {df_updated.shape[0]:,} rows x {df_updated.shape[1]} columns\n")
print("="*65)
print("  NUMERICAL SUMMARY STATISTICS")
print("="*65)
summary = df_updated[num_cols].describe().T
summary['skewness'] = df_updated[num_cols].skew()
summary['missing']  = df_updated[num_cols].isna().sum()
print(summary.round(2).to_string())

print("\n"+"="*65)
print("  CATEGORICAL SUMMARY")
print("="*65)

#Showing of Barcharts and Histograms with key attributes
fig, axes = plt.subplots(2, 4, figsize=(22, 10))
fig.suptitle("Fig 1 — Numerical Feature Distributions", fontsize=16, y=1.01)
axes = axes.flatten()
for i, col in enumerate(num_cols):
    ax = axes[i]
    data = df_updated[col].dropna()
    n_bins = 15 if col in ['Prod_Rating','Delivery/Service_Rating','Qty','Coupon_Discount'] else 35
    ax.hist(data, bins=n_bins, color=PALETTE[i], edgecolor='white', linewidth=0.5, alpha=0.88)
    mv, mdv = data.mean(), data.median()
    ax.axvline(mv,  color=RED,   ls='--', lw=1.8, label=f'Mean {mv:.1f}')
    ax.axvline(mdv, color=GREEN, ls=':',  lw=1.8, label=f'Median {mdv:.1f}')
    ax.set_title(col); ax.set_xlabel(col); ax.set_ylabel("Count")
    ax.legend(fontsize=8, framealpha=0.75)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
axes[-1].set_visible(False)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
#Analysis of Attributes
fig, axes = plt.subplots(2, 4, figsize=(26, 12))
fig.suptitle("Fig 2 — Categorical Feature Distributions", fontsize=16, y=1.01)
axes = axes.flatten()
for i, col in enumerate(cat_cols):
    ax = axes[i]
    vc = df_updated[col].value_counts(dropna=False).head(12)
    vc.index = vc.index.fillna('(missing)').astype(str)
    colors = [PALETTE[j % len(PALETTE)] for j in range(len(vc))]
    bars = ax.barh(vc.index[::-1], vc.values[::-1],
                   color=colors[::-1], edgecolor='white', linewidth=0.4)
    for bar, val in zip(bars, vc.values[::-1]):
        ax.text(bar.get_width() + vc.values.max()*0.015,
                bar.get_y() + bar.get_height()/2,
                f'{val:,}', va='center', fontsize=8)
    ax.set_title(col); ax.set_xlabel("Count")
    ax.set_xlim(0, vc.values.max()*1.18)
    ax.tick_params(axis='y', labelsize=8)
plt.tight_layout()
plt.show()

#Rating Analysis
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Fig 3 — Ratings Analysis", fontsize=15)

vc = df_updated['Prod_Rating'].value_counts().sort_index()
bars = axes[0].bar(vc.index, vc.values, color=PALETTE[:5], edgecolor='white', width=0.6)
for bar, val in zip(bars, vc.values):
    axes[0].text(bar.get_x()+bar.get_width()/2, bar.get_height()+20,
                 f'{val:,}', ha='center', fontsize=9, fontweight='bold')
axes[0].set_title("Product Rating Distribution")
axes[0].set_xlabel("Rating (1-5)"); axes[0].set_ylabel("Count"); axes[0].set_xticks([1,2,3,4,5])

vc2 = df_updated['Delivery/Service_Rating'].value_counts().sort_index()
bars2 = axes[1].bar(vc2.index, vc2.values, color=PALETTE[5:10], edgecolor='white', width=0.6)
for bar, val in zip(bars2, vc2.values):
    axes[1].text(bar.get_x()+bar.get_width()/2, bar.get_height()+20,
                 f'{val:,}', ha='center', fontsize=9, fontweight='bold')
axes[1].set_title("Delivery/Service Rating Distribution")
axes[1].set_xlabel("Rating (1-5)"); axes[1].set_ylabel("Count"); axes[1].set_xticks([1,2,3,4,5])

cat_rating = df_updated.groupby('Category')['Prod_Rating'].mean().sort_values()
bars3 = axes[2].barh(cat_rating.index, cat_rating.values,
                     color=[PALETTE[j%len(PALETTE)] for j in range(len(cat_rating))], edgecolor='white')
for bar, val in zip(bars3, cat_rating.values):
    axes[2].text(bar.get_width()+0.02, bar.get_y()+bar.get_height()/2,
                 f'{val:.2f}', va='center', fontsize=8)
axes[2].set_title("Avg Product Rating by Category")
axes[2].set_xlabel("Avg Rating"); axes[2].set_xlim(0, cat_rating.max()*1.12)
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Fig 4 — Price & Order Amount Analysis", fontsize=15)

axes[0].hist(df_updated['Price'].dropna(), bins=40, color=BLUE, edgecolor='white', alpha=0.85)
axes[0].axvline(df_updated['Price'].mean(),   color=RED,   ls='--', lw=2, label=f"Mean Rs{df_updated['Price'].mean():.0f}")
axes[0].axvline(df_updated['Price'].median(), color=GREEN, ls=':',  lw=2, label=f"Median Rs{df_updated['Price'].median():.0f}")
axes[0].set_title("Product Price Distribution"); axes[0].set_xlabel("Price (Rs)"); axes[0].set_ylabel("Count")
axes[0].legend(fontsize=9)

axes[1].hist(df_updated['Order_Amount'].dropna(), bins=40, color=ORANGE, edgecolor='white', alpha=0.85)
axes[1].axvline(df_updated['Order_Amount'].mean(),   color=RED,   ls='--', lw=2, label=f"Mean Rs{df_updated['Order_Amount'].mean():.0f}")
axes[1].axvline(df_updated['Order_Amount'].median(), color=GREEN, ls=':',  lw=2, label=f"Median Rs{df_updated['Order_Amount'].median():.0f}")
axes[1].set_title("Order Amount Distribution"); axes[1].set_xlabel("Order Amount (Rs)"); axes[1].set_ylabel("Count")
axes[1].legend(fontsize=9)

cat_amt = df_updated.groupby('Category')['Order_Amount'].mean().sort_values()
bars = axes[2].barh(cat_amt.index, cat_amt.values,
                    color=[PALETTE[j%len(PALETTE)] for j in range(len(cat_amt))], edgecolor='white')
for bar, val in zip(bars, cat_amt.values):
    axes[2].text(bar.get_width()+cat_amt.max()*0.01, bar.get_y()+bar.get_height()/2,
                 f'Rs{val:.0f}', va='center', fontsize=8)
axes[2].set_title("Avg Order Amount by Category"); axes[2].set_xlabel("Avg Order Amount (Rs)")
axes[2].set_xlim(0, cat_amt.max()*1.15)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import plotly.graph_objects as go

# Load dataset
df = pd.read_excel("/content/Updated_Zepto_Dataset.xlsx")

# Create Order Value column
df["Order_Value"] = df["Price"] * df["Qty"]

# --------------------------------
# 1. Scatter Plot (Age vs Spending)
# --------------------------------
plt.figure()

plt.scatter(df["Age"], df["Order_Value"])

plt.xlabel("Customer Age")
plt.ylabel("Order Value")
plt.title("Customer Age vs Spending")

plt.show()


# --------------------------------
# 2. Hexbin Density Plot
# --------------------------------
plt.figure()

plt.hexbin(df["Price"], df["Qty"], gridsize=30)

plt.xlabel("Product Price")
plt.ylabel("Quantity Purchased")
plt.title("Price vs Quantity Density")

plt.colorbar()

plt.show()

#Shankey Chart
flow_df = df.groupby(["Category","Brand","Transaction_Mode"]).size().reset_index(name="count")

labels = list(pd.concat([
    flow_df["Category"],
    flow_df["Brand"],
    flow_df["Transaction_Mode"]
]).unique())

label_index = {label:i for i,label in enumerate(labels)}

source = flow_df["Category"].map(label_index)
target = flow_df["Brand"].map(label_index)
value = flow_df["count"]

fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels),
    link=dict(source=source, target=target, value=value)
)])

fig.update_layout(title_text="Customer Purchase Flow: Category → Brand")
fig.show()

# --------------------------------
# 4. Correlation Heatmap
# --------------------------------
numeric_df = df[[
    "Age",
    "Price",
    "Qty",
    "Coupon_Discount",
    "Prod_Rating",
    "Delivery/Service_Rating",
    "Order_Value"
]]

corr = numeric_df.corr()

plt.figure()

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")

plt.show()


# --------------------------------
# 5. Pair Plot (MULTI VARIABLE ANALYSIS)
# --------------------------------
pair_df = df[[
    "Age",
    "Price",
    "Qty",
    "Coupon_Discount",
    "Prod_Rating",
    "Delivery/Service_Rating",
    "Order_Value"
]]

sns.pairplot(pair_df)

plt.show()


# --------------------------------
# 6. Treemap (Category Sales)
# --------------------------------
category_sales = df.groupby("Category")["Order_Value"].sum().reset_index()

plt.figure()
colors = [
    "#FF6B6B",
    "#4ECDC4",
    "#45B7D1",
    "#FFA07A",
    "#98D8C8",
    "#F7DC6F",
    "#BB8FCE"
]
squarify.plot(
    sizes=category_sales["Order_Value"],
    label=category_sales["Category"],
    color = colors,
    alpha=0.8
)

plt.title("Treemap of Sales by Category")

plt.axis("off")

plt.show()