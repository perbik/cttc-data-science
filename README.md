# 📊 Sales Data Cleaning and Visualization

## Overview

This project focuses on cleaning and analyzing a messy sales dataset using Python. It demonstrates essential data preprocessing techniques and generates visual insights through multiple charts.

## Features

- ✅ Handles missing values using mean imputation
- ✅ Converts inconsistent data types (strings → numeric, datetime)
- ✅ Cleans currency and percentage formats
- ✅ Standardizes categorical values (Region, Product, Category)
- ✅ Generates multiple visualizations (by Region, Trends, Category Distribution)

## Installation

Install the required dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

## Project Structure

```
cttc-data-science/
├── README.md
├── data/
│   └── messy_sales.csv
└── src/
    └── main.py
    └── visualization.py
    └── data_cleaning.py
```

## Usage

Run the script from the project root:

```bash
python src/main.py
```

The script expects the dataset at `data/messy_sales.csv`.

## Data Cleaning Steps

The script performs the following preprocessing operations:

1. **Column Cleaning** — Removes whitespace from column names
2. **Type Conversion** — Converts Units Sold and Total Sales to numeric; Date to datetime
3. **Missing Values** — Fills missing values using mean imputation
4. **Format Cleaning** — Removes currency symbols ($, USD) and percentage formats
5. **Standardization** — Normalizes text formatting and fixes inconsistent labels (e.g., Elec → Electronics)

## Visualizations

The script generates three interactive charts:

| Chart                   | Type       | Description                     |
| ----------------------- | ---------- | ------------------------------- |
| Total Sales by Region   | Bar Chart  | Regional performance comparison |
| Sales Trend Over Time   | Line Chart | Time-based sales patterns       |
| Sales Share by Category | Pie Chart  | Category distribution breakdown |

All visualizations are displayed in a single window, automatically centered on screen.
