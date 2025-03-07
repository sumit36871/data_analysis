import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def generate_insights(data):
    insights = {}
    insights["Number of Rows"] = data.shape[0]
    insights["Number of Columns"] = data.shape[1]
    insights["Missing Values"] = data.isnull().sum().sum()
    insights["Duplicate Rows"] = data.duplicated().sum()
    insights["Data Types"] = data.dtypes.to_dict()
    return insights

def visualize_data(data):
    numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
    visualization_insights = {}

    if numeric_columns:
        st.write("### Numeric Columns Distribution")
        for col in numeric_columns:
            plt.figure(figsize=(10, 5))
            sns.histplot(data[col], kde=True)
            plt.title(f'Distribution of {col}')
            st.pyplot(plt)
            visualization_insights[col] = generate_visualization_insights(data[col])
    
    if categorical_columns:
        st.write("### Categorical Columns Distribution")
        for col in categorical_columns:
            plt.figure(figsize=(10, 5))
            sns.countplot(y=data[col])
            plt.title(f'Distribution of {col}')
            st.pyplot(plt)
            visualization_insights[col] = generate_visualization_insights(data[col])

    # Visualize RAG status
    if "status" in data.columns:
        st.write("### RAG Status Distribution")
        plt.figure(figsize=(10, 5))
        sns.countplot(x=data["status"], palette={"Red": "red", "Amber": "orange", "Green": "green"})
        plt.title('RAG Status Distribution')
        st.pyplot(plt)
        visualization_insights["status"] = generate_visualization_insights(data["status"])

    return visualization_insights

def generate_visualization_insights(series):
    insights = {}
    if series.dtype == 'object':
        value_counts = series.value_counts()
        insights["Most Frequent"] = value_counts.idxmax()
        insights["Frequency"] = value_counts.max()
    elif pd.api.types.is_numeric_dtype(series):
        insights["Mean"] = series.mean()
        insights["Median"] = series.median()
        insights["Standard Deviation"] = series.std()
        insights["Minimum"] = series.min()
        insights["Maximum"] = series.max()
    return insights