import streamlit as st
import pandas as pd
import pickle as pkl
from sklearn.preprocessing import LabelEncoder

st.title('Diamond Price Prediction')
st.subheader('Please fill in the details of the diamond')

carat = st.number_input('carat', min_value=0.00, max_value=5.00, value=2.5, step=0.01)
color = st.selectbox('color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
y = st.number_input('y', min_value=0.0, max_value=10.00, value=5.00, step=0.01)

input_data = {'carat': carat, 'color': color, 'y': y}
input_df = pd.DataFrame([input_data])

with open('clr_le.pkl', 'rb') as file:
    clr_le = pkl.load(file)

input_df['color'] = clr_le.transform(input_df['color'])

# Ensure input_df has the correct columns
expected_columns = ['carat', 'color', 'y']
input_df = input_df.reindex(columns=expected_columns, fill_value=0)

with open('model.pkl', 'rb') as file:
    model = pkl.load(file)

if st.button('Predict'):
    prediction = model.predict(input_df)
    st.write('The predicted price of the diamond is:', prediction[0])