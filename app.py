import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Your Data Analyst Agent")

uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())
    x_axis = st.selectbox("Choose X-axis column", df.columns)
    y_axis = st.selectbox("Choose Y-axis column", df.columns)

    fig, ax = plt.subplots()
    sns.boxplot(x=x_axis, y=y_axis, data=df, ax=ax)
    st.pyplot(fig)
