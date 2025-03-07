
import streamlit as st
import pandas as pd
from data_analysis.data_analysis import generate_insights, visualize_data, generate_visualization_insights

st.title("Data Analysis Project")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Load data
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.write("## Data Preview")
    st.write(data.head())

    # Generate insights
    insights = generate_insights(data)
    st.write("## Data Insights")
    st.write(insights)

    # Visualize data and generate insights from visualizations
    st.write("## Data Visualization")
    visualization_insights = visualize_data(data)
    
    st.write("## Visualization Insights")
    st.write(visualization_insights)
else:
    st.write("Please upload a data file.")