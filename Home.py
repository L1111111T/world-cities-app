import streamlit as st

MAIN_APP_PAGE = "pages/app.py"

st.set_page_config(page_title="World Cities App", page_icon="🌍")

st.title("World Cities App")
st.write("Welcome! Use the button below to open the main app page.")

if st.button("Go to App"):
    st.switch_page(MAIN_APP_PAGE)
