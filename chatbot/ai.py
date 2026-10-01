import streamlit as st

st.title(" Welcome to AI Chatbot")
prompt = st.text_input("Enter your message:")

if st.button("Send"):

    if not prompt():
        st.warning(" Please enter a message.")

    else:
        st.success(" Message received successfully!")
        st.subheader("AI Response")
        st.write("Your message was:", prompt)