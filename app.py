import streamlit as st
import pandas as pd

st.title("Mall Customer Segmentation Dashboard")

# Load data
df = pd.read_csv("Mall_Customers.csv")

# Show raw data
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Simple filter example
gender = st.selectbox("Select Gender", options=["All", "Male", "Female"])
if gender != "All":
    df = df[df["Gender"] == gender]

st.subheader(f"Customers: {len(df)}")
st.dataframe(df)

# Add any charts or segmentation logic here
