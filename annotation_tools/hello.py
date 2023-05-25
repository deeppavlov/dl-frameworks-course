import streamlit as st
import pandas as pd

st.title('My Streamlit App')

st.write('Welcome to my first Streamlit app!')

name = st.text_input('Enter your name', 'John Doe') #окно для ввода текста
age = st.slider('Select your age', 0, 100, 25)
submitted = st.button('Submit')

if submitted:
    st.write(f'Hello {name}, your age is {age}!')


data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 2, 5]})
st.line_chart(data)

