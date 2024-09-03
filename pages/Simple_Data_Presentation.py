import io
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from models.ml_models import preprocess_data

# Upload a CSV file
st.title("Titanic Data Analysis")
upload_file = st.file_uploader("Upload the Titanic CSV file", type=["csv"])

if upload_file is not None:
    data = pd.read_csv(upload_file)

    # Check if all required columns are present
    required_columns = [
        'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch',
        'Ticket', 'Fare', 'Cabin', 'Embarked'
    ]

    if all(col in data.columns for col in required_columns):

        # Display summary statistics
        if st.checkbox("Show summary statistics"):
            st.subheader("Summary Statistics")
            st.write(data.describe())

        # Display information about the data
        if st.checkbox("Show data information"):
            st.subheader("Data Information")
            buffer = io.StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)

        # Display the data preview
        if st.checkbox("Show data preview"):
            st.subheader("Data Preview")
            st.write(data)

        # Filter data by specific column values
        st.subheader("Filter Data")
        cols = data.columns.tolist()
        selected_col = st.selectbox("Select a column to filter by", cols)
        if selected_col:
            unique_values = data[selected_col].unique()
            selected_value = st.selectbox(f"Select a value from '{selected_col}'", unique_values)
            if selected_value is not None:
                filtered_data = data[data[selected_col] == selected_value]
                st.write(filtered_data)
            else:
                st.warning("Please select a value to filter by.")

        # Data Visualization
        st.subheader("Data Visualization")
        x_col = st.selectbox("Select X-axis for plotting", cols)
        y_col = st.selectbox("Select Y-axis for plotting", cols)

        if st.button("Generate Plot"):
            if not filtered_data.empty:
                plt.figure(figsize=(10, 6))
                plt.scatter(filtered_data[x_col], filtered_data[y_col], alpha=0.5)
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.title(f'Scatter plot of {y_col} vs {x_col}')
                st.pyplot(plt)
            else:
                st.warning("Filtered data is empty. Please adjust your filters.")

        # Display missing values
        st.subheader("Missing Values")
        missing_values = data.isnull().sum().sort_values(ascending=False)
        st.write(missing_values)

        # Preprocess and display transformed data
        data = preprocess_data(data)
        st.subheader("Transformed Data")
        st.write(data)

    else:
        st.error("The uploaded file does not contain the required columns.")
else:
    st.info("Please upload a CSV file to start the analysis.")