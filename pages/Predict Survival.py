import streamlit as st
import pandas as pd
from joblib import load


age = st.sidebar.slider('Age', 0, 100, 25)
sex = st.sidebar.selectbox('Sex', ('male', 'female'))
pclass = st.sidebar.selectbox('Passenger Class', (1, 2, 3))
siblings_spouses = st.sidebar.slider('Siblings/Spouses Aboard', 0, 10, 0)
parents_children = st.sidebar.slider('Parents/Children Aboard', 0, 10, 0)
embarked = st.sidebar.selectbox('Port of Embarkation', ('Cherbourg', 'Queenstown', 'Southampton'))
fare = st.sidebar.slider('Fare', 0.0, 500.0, 50.0)
button = st.sidebar.button('Predict')
embarked_c, embarked_q, embarked_s = 0, 0, 0
if embarked == 'Cherbourg':
    embarked_c = 1
elif embarked == 'Queenstown':
    embarked_q = 1
else:
    embarked_s = 1
data = {
    'Pclass': pclass,
    'Sex': 1 if sex == 'male' else 0,
    'Age': age,
    'SibSp': siblings_spouses,
    'Parch': parents_children,
    'Fare': fare,
    'Embarked_C': embarked_c,
    'Embarked_Q': embarked_q,
    'Embarked_S': embarked_s
}
features = pd.DataFrame(data, index=[0])

print(features.columns)

if button:
    # Display the user input data
    st.subheader('User Input Data')
    st.write(features)

    st.markdown("---")  # Adds a horizontal line for separation

    # Load the model
    model = load('models/best_model.joblib')

    # Make a prediction based on user input
    prediction = model.predict(features)

    # Display the prediction result
    st.subheader('Prediction')
    result_text = 'Survived' if prediction[0] == 1 else 'Did not survive'

    # Optionally, add some formatting to the prediction result
    if prediction[0] == 1:
        st.success(result_text)
    else:
        st.error(result_text)
