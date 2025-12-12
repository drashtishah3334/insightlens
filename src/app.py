import streamlit as st
import pandas as pd

st.set_page_config(page_title="InsightLens - CSV Insights", layout="wide")

st.title("📊 InsightLens – CSV Preview")

st.write(
    "Upload a CSV file to get started. "
    "For now, we'll simply load it and show the first few rows."
)

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"File uploaded successfully! Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        st.subheader("Preview of the data")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Oops, something went wrong while reading the file: {e}")
