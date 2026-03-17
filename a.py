import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Data Analysis App", layout="wide")
st.title("📊 Data Analysis App")
st.write("Upload any CSV file and analyze it easily")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    dataset = pd.read_csv(uploaded_file)
    st.subheader("📄 Dataset Preview")
    st.write(dataset.head())
    st.write("📌 Shape:", dataset.shape)
    numeric_data = dataset.select_dtypes(include=np.number)
    st.subheader("📊 Mean Values")
    mean_values = numeric_data.mean()
    st.write(mean_values)
    st.subheader("📈 Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.write("🔹 Line Graph")
        plt.figure(figsize=(4, 3))
        plt.plot(numeric_data)
        plt.title("Line Graph")
        plt.grid()
        st.pyplot(plt)
    with col2:
        st.write("🔹 Bar Graph")
        plt.figure(figsize=(4, 3))
        plt.bar(mean_values.index, mean_values.values)
        plt.xticks(rotation=45)
        plt.title("Mean Values")
        st.pyplot(plt)
    col3, col4 = st.columns(2)
    with col3:
        st.write("🔹 Histogram")
        plt.figure(figsize=(4, 3))
        numeric_data.hist()
        plt.title("Distribution")
        st.pyplot(plt)
    with col4:
        st.write("🔹 Scatter Plot")
        if len(numeric_data.columns) >= 2:
            plt.figure(figsize=(4, 3))
            x = numeric_data.iloc[:, 0]
            y = numeric_data.iloc[:, 1]
            plt.scatter(x, y)
            plt.xlabel(numeric_data.columns[0])
            plt.ylabel(numeric_data.columns[1])
            plt.title("Scatter Plot")
            st.pyplot(plt)
        else:
            st.write("Not enough numeric columns")
    st.subheader("📌 Correlation")
    correlation = dataset.corr(numeric_only=True)
    st.write(correlation)
    plt.figure(figsize=(5, 4))
    plt.imshow(correlation)
    plt.colorbar()
    plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
    plt.yticks(range(len(correlation.columns)), correlation.columns)
    plt.title("Heatmap")
    st.pyplot(plt)
else:
    st.warning("⚠ Please upload a CSV file")