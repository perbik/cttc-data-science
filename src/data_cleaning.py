import pandas as pd
import numpy as np


def clean_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    # Strip column names
    df.columns = df.columns.str.strip()

    # Convert numeric columns
    df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')
    df['Total Sales'] = pd.to_numeric(df['Total Sales'], errors='coerce')

    # Fill missing values
    df['Units Sold'] = df['Units Sold'].fillna(df['Units Sold'].mean())
    df['Total Sales'] = df['Total Sales'].fillna(df['Total Sales'].mean())

    # Convert date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Clean text columns
    for col in ['Region', 'Product', 'Category']:
        df[col] = df[col].astype(str).str.strip().str.title()

    # Clean currency columns
    for col in ['Unit Price', 'Total Sales']:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("[$, USD]", "", regex=True)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Clean profit margin
    df['Profit Margin (%)'] = (
        df['Profit Margin (%)']
        .astype(str)
        .str.replace("%", "", regex=True)
        .str.replace("percent", "", regex=True)
        .astype(float)
    )

    df['Profit Margin (%)'] = np.where(
        df['Profit Margin (%)'] < 1,
        df['Profit Margin (%)'] * 100,
        df['Profit Margin (%)']
    )

    # Fix categories
    df['Category'] = df['Category'].replace({
        'Elec': 'Electronics',
        'Gadget': 'Gadgets'
    })

    # Drop critical missing values
    df_cleaned = df.dropna(subset=['Date', 'Total Sales', 'Region'])

    return df_cleaned