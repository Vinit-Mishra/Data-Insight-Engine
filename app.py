import streamlit as st
import pandas as pd
# Importing functions from your provided utils file
# Ensure 'utils (1).py' is renamed to 'utils.py'
from utils import summarize_data, plot_numeric_data, plot_categorical_data

# Page Configuration
st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("📊 Automated Data Analysis Dashboard")
st.markdown("Upload a CSV file to generate automated summaries and visualizations.")

# 1. File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the data
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        
        # Display Raw Data
        with st.expander("View Raw Data"):
            st.dataframe(df.head())

        # 2. Data Summary
        st.header("1. Statistical Summary")
        # Uses summarize_data from utils.py
        summary = summarize_data(df)
        st.dataframe(summary)

        # 3. Visualizations
        st.header("2. Data Visualizations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Numeric Distributions")
            # Uses plot_numeric_data from utils.py
            try:
                fig_num = plot_numeric_data(df)
                st.pyplot(fig_num)
            except Exception as e:
                st.info("No numeric data to plot or error in plotting.")

        with col2:
            st.subheader("Categorical Counts")
            # Uses plot_categorical_data from utils.py
            try:
                fig_cat = plot_categorical_data(df)
                st.pyplot(fig_cat)
            except Exception as e:
                st.info("No categorical data to plot or error in plotting.")

    except Exception as e:
        st.error(f"Error reading the file: {e}")

else:
    st.info("Awaiting CSV file upload...")