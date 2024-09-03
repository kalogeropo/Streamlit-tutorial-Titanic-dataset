import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Titanic Survival Prediction Project",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title of the project
st.title("🚢 Titanic Survival Prediction Project")

# Project description
st.write("""
## Welcome to the Titanic Survival Prediction Project!

This web application allows you to explore and analyze the Titanic dataset, 
one of the most famous datasets in the world of data science. 

### Project Overview
The Titanic Survival Prediction Project is designed to:
- **Analyze the Titanic Dataset**: View summary statistics, missing values, and detailed information about the passengers aboard the Titanic.
- **Visualize Data**: Generate plots to understand relationships between different features, such as age, fare, and survival rate.
- **Predict Survival**: Use a pre-trained machine learning model to predict whether a passenger would have survived based on their features.

### Machine Learning Model
A **Random Forest Classifier** was trained on the Titanic dataset using various hyperparameters to find the best model. After fine-tuning, the model achieved an accuracy of **around 83%** on the test data. 

This means that the model correctly predicted the survival of passengers with an accuracy of 83%, making it a reliable tool for exploring the survival chances of passengers based on their characteristics.

### Key Features
- **Data Exploration**: Upload your own Titanic CSV file and explore the data with ease. 
- **Data Preprocessing**: Automatic preprocessing of the data to handle missing values and encode categorical variables.
- **Machine Learning Prediction**: After preprocessing, the app can predict the survival of passengers using a machine learning model trained on the Titanic dataset.

### How to Use the App
1. **Upload Data**: Start by uploading the Titanic CSV file.
2. **Explore Data**: Use the sidebar option Simple Data Presentation to view data summaries, filter data, and visualize relationships.
3. **Predict Survival**: Input passenger features to see if they would have survived.

### About the Titanic Dataset
The Titanic dataset provides information on the fate of passengers on the Titanic, summarized according to economic status (class), sex, age, and survival. It is a great starting point for learning about data science and machine learning.

### Get Started!
Use the sidebar to navigate through the different sections of the application. 
Enjoy exploring the data and making predictions!

---

This project is powered by **Streamlit** and **scikit-learn**.
""")

# Footer
st.markdown("---")
st.write("Developed by Kalogeropoulos Nikitas-Rigas | © 2024 Streamlit Tutorial Project")
