import pandas as pd
import matplotlib.pyplot as plt

try:
    try:
        df = pd.read_csv("SalesDataset.csv", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv("SalesDataset.csv", encoding="latin1")

    # Show available columns
    print("\nColumns in Dataset:")
    print(df.columns.tolist())

    # Check if Date and Sales columns exist
    if 'Date' not in df.columns:
        print("ERROR: 'Date' column not found.")
        exit()

    if 'Sales' not in df.columns:
        print("ERROR: 'Sales' column not found.")
        exit()

    # Convert Date Column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove invalid dates
    df = df.dropna(subset=['Date'])

    # Dataset Information
    print("\nDataset Information")
    print(df.info())

    print("\nStatistical Summary")
    print(df.describe())

    # Check Missing Values
    print("\nMissing Values")
    print(df.isnull().sum())

    # Plot Sales Trend
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Sales'], marker='o')
    plt.title("Historical Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.show()

except FileNotFoundError:
    print("ERROR: SalesDataset.csv file not found.")
except Exception as e:
    print("ERROR:", e)