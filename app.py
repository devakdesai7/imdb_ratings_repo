import streamlit as st

from pages.analytics import analytics

st.set_page_config(layout="wide")

page = st.sidebar.selectbox(
    "☰ Navigation",
    ['Home', 'Analytics', 'About']
)

if page == 'Analytics':
    analytics()







