import streamlit as st

MAIN_APP_PAGE = "pages/app.py"
MAIN_APP_PAGE_FALLBACK = "pages/app"

st.set_page_config(page_title="World Cities App", page_icon="🌍")

st.title("World Cities App")
st.write("Welcome! Use the button below to open the main app page.")

if st.button("Go to App"):
    try:
        st.switch_page(MAIN_APP_PAGE)
    except Exception:
        st.switch_page(MAIN_APP_PAGE_FALLBACK)
