import pandas as pd

try:
    df = pd.read_csv("SalesDataset.csv", encoding="latin1")
    print(df.head())
    print(df.columns)
except Exception as e:
    print(e)