import io

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Dashboard")

upload_file = st.file_uploader("Upload the Titanic CSV file", type=["csv"]) # upload a csv file

if upload_file is not None:
    data = pd.read_csv(upload_file)
    check_cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',
                  'Cabin', 'Embarked']

    if all(col in data.columns for col in check_cols):
        if st.checkbox("Show summary"):
            st.write(data.describe())
        if st.checkbox("Show info"):
            buffer = io.StringIO()
            data.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)

        if st.checkbox("Show data"):
            st.subheader("Data Preview")
            st.write(data)

        cols = data.columns.tolist()
        selected_cols = st.selectbox("Select columns to filter", cols)
        uniques = data[selected_cols].unique()
        selected_unique = st.selectbox("Select unique values", uniques)
        filtered = data[data[selected_cols] == selected_unique]
        st.write(filtered)

        st.subheader("Data Visualization")
        x_col = st.selectbox("Select X-axis", cols)
        y_col = st.selectbox("Select Y-axis", cols)

        if st.button("Generate Plot"):
            st.scatter_chart(filtered.set_index(x_col)[y_col])

        st.subheader("Missing Values")
        st.write(data.isnull().sum().sort_values(ascending=False))
        data["Age"] = data["Age"].fillna(data["Age"].mean())
        data["Cabin"] = data["Cabin"].fillna('U')
        data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
        data['Sex'] = data['Sex'].map({'female': 0, 'male': 1})

        data = pd.get_dummies(data, columns=["Embarked"])
        deck_set = data["Cabin"].str[0]
        data['Cabin'] = deck_set
        unique_list = list(data.Cabin.unique())
        mapping = {item: unique_list.index(item) for item in unique_list}
        data['Cabin'] = data['Cabin'].map(mapping)

        data = data.drop(['Ticket'], axis=1)
        data = data.drop(['Name'], axis=1)
        st.subheader("Transformed Data")
        st.write(data)
    else:
        st.write("Invalid file")
        upload_file = None
else:
    st.write("Please upload a file")