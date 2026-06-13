import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Predictive Analytics Dashboard")

file = st.file_uploader("Upload Sales Dataset", type=["csv"])

if file is not None:

    try:
        # Read CSV with different encodings
        try:
            df = pd.read_csv(file, encoding="utf-8")
        except UnicodeDecodeError:
            file.seek(0)
            df = pd.read_csv(file, encoding="latin1")

        st.success("Dataset Loaded Successfully!")

        # Show dataset
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        # Show available columns
        st.subheader("Available Columns")
        st.write(df.columns.tolist())

        # User selects columns
        date_column = st.selectbox(
            "Select the Date Column",
            df.columns
        )

        sales_column = st.selectbox(
            "Select the Sales Column",
            df.columns
        )

        # Convert date column
        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        )

        # Remove invalid dates
        df = df.dropna(subset=[date_column])

        # Statistics
        st.subheader("Dataset Statistics")
        st.write(df.describe())

        # Missing Values
        st.subheader("Missing Values")
        st.write(df.isnull().sum())

        # Graph
        st.subheader("Sales Trend Analysis")

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            df[date_column],
            df[sales_column],
            marker="o"
        )

        ax.set_title("Sales Trend")
        ax.set_xlabel(date_column)
        ax.set_ylabel(sales_column)
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")