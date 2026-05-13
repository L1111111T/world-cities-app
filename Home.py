import streamlit as st

st.set_page_config(page_title="World Cities App", page_icon="🌍")

st.title("World Cities App")
st.write("Welcome! Use the button below to open the main app page.")

if st.button("Go to App"):
    st.switch_page("pages/app.py")
