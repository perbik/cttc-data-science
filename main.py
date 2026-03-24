import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
print(sys.executable)

df = pd.read_csv("messy_sales.csv")
df.head(10)

df.info()

df.isnull().sum()

df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')
df['Total Sales'] = pd.to_numeric(df['Total Sales'], errors='coerce')

df['Units Sold'] = df['Units Sold'].fillna(df["Units Sold"].mean())
df['Total Sales'] = df['Total Sales'].fillna(df["Total Sales"].mean())

df.columns = df.columns.str.strip()

df['Date'] = pd.to_datetime(df["Date"], errors = "coerce")

for col in ['Region', 'Product', 'Category']:
  df[col] = df[col].str.strip().str.title()

df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')

for col in ['Unit Price', 'Total Sales']:
  df[col] = df[col].astype(str)
  df[col] = (
      df[col]
        .str.replace("[$, USD]", "", regex=True)
        .str.strip()
  )
  df[col] = pd.to_numeric(df[col], errors = "coerce")

df['Profit Margin (%)'] = (
    df['Profit Margin (%)']
      .astype(str)
      .str.replace("%", "", regex=True)
      .str.replace("percent", "", regex=True)
      .astype(float)
)
df['Profit Margin (%)'] = np.where(df['Profit Margin (%)'] < 1, df['Profit Margin (%)'] * 100, df['Profit Margin (%)'])

for col in ['Category']:
  df[col] = df[col].replace('Elec', 'Electronics')
  df[col] = df[col].replace('Gadget', 'Gadgets')

df_cleaned = df.dropna(subset = ['Date', 'Total Sales', 'Region'])

df_cleaned.head(15)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# --- Bar Chart ---
sns.barplot(data=df_cleaned, x='Region', y='Total Sales', estimator=sum, ax=axes[0,0])
axes[0,0].set_title('Total Sales by Region')
axes[0,0].tick_params(axis='x', rotation=30)

# --- Line Chart ---
df_cleaned.groupby('Date')['Total Sales'].sum().plot(ax=axes[0,1])
axes[0,1].set_title('Sales Trend Over Time')

# --- Pie Chart (centered better) ---
category_sales = df_cleaned.groupby('Category')['Total Sales'].sum()
category_sales.plot(kind='pie', autopct='%1.1f%%', ax=axes[1,0])
axes[1,0].set_title('Sales Share by Category')
axes[1,0].set_ylabel('')

# --- Remove empty subplot ---
axes[1,1].axis('off')

plt.tight_layout()

manager = plt.get_current_fig_manager()
window = manager.window

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Window size
width = 1000
height = 700

# Calculate center position
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# Set window position
window.geometry(f"{width}x{height}+{x}+{y}")

plt.show()