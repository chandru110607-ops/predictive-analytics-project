import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

try:
    # Read CSV using different encodings
    try:
        df = pd.read_csv("SalesDataset.csv", encoding="utf-8")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv("SalesDataset.csv", encoding="latin1")
        except UnicodeDecodeError:
            df = pd.read_csv("SalesDataset.csv", encoding="cp1252")

    print("Dataset Loaded Successfully!")

    print("\nColumns in Dataset:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    # Check required columns
    if 'Date' not in df.columns:
        print("\nERROR: 'Date' column not found.")
        print("Available columns:", df.columns.tolist())
        exit()

    if 'Sales' not in df.columns:
        print("\nERROR: 'Sales' column not found.")
        print("Available columns:", df.columns.tolist())
        exit()

    # Convert Date Column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove invalid dates
    df = df.dropna(subset=['Date'])

    # Remove missing sales values
    df = df.dropna(subset=['Sales'])

    # Feature Engineering
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # Features and Target
    X = df[['Year', 'Month', 'Day']]
    y = df['Sales']

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Accuracy
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\n===== MODEL RESULTS =====")
    print("MAE:", round(mae, 2))
    print("R2 Score:", round(r2, 2))

    # Future Prediction
    future_date = pd.DataFrame({
        'Year': [2026],
        'Month': [12],
        'Day': [25]
    })

    future_sales = model.predict(future_date)

    print("\nPredicted Sales on 25-Dec-2026:")
    print(round(future_sales[0], 2))

except FileNotFoundError:
    print("\nERROR: File not found.")
    print("Make sure 'SalesDataset.csv' is in the same folder as this Python file.")

except Exception as e:
    print("\nERROR:")
    print(str(e))