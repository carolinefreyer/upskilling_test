import streamlit as st

# Create a title and text in the app
st.title('My Streamlit App')
st.write('This is a simple Streamlit web app.')

# Add a slider widget for user input
user_input = st.slider('Select a value:', 0, 100, 50)

# Display the user input
st.write('You selected:', user_input)