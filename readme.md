# 🏠 Real Estate Management System

A Python CLI app for managing real estate data using MySQL and Excel.

## 📦 Features

- Add/Delete/Search property data
- View statistics on rent prices
- Visualize property rent with bar charts
- Excel to MySQL import
- Group filter based on type/location

## 🛠 Tech Stack

- Python
- MySQL
- `mysql-connector-python`
- `openpyxl`
- `matplotlib`, `numpy`, `pandas`

## 🧰 Prerequisites

- Python 3.x
- MySQL Server running
- Place your Excel file in:  
  `C:\Users\logun\OneDrive\Documents\PropEase\realestae23.xlsx`

## 🚀 Setup

1. **Install dependencies**:
   ```bash
   pip install mysql-connector-python openpyxl matplotlib numpy pandas

2. **Create DB**:
    ```sql
    CREATE DATABASE real_estate_management;

3. **Run**:
    ```bash
    python main.py



## 📊 Excel Format
    property_id | property_type | location | listing_price | rent_price | owner_name | owner_contact | status | listing_date | last_updated | dditional_comments
