import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd

st.title('Welcome to Obesity Detector')
age = st.slider('Age',10,112)
gender = st.selectbox('Gender',['Male','Female'])
height = st.number_input('Height',120,210)
weight = st.number_input('Weight', 10,120)
bmi = st.number_input('BMI',weight/((height/100)**2))

input_data = {
    'Age': [age],
    'Gender': [gender],
    'Height':[height],
    'Weight': [height],
    'Weight':[weight],
    'BMI':[bmi]
}
input_df = pd.DataFrame(input_data)
encoder = LabelEncoder()
input_df['Gender'] = encoder.fit_transform(input_df['Gender'])

with open('obesity_model.h5', 'rb') as file:
    model = pickle.load(file)

prediction = model.predict(input_df)
st.write("Prediction:", prediction[0])
