import streamlit as st
import pandas as pd

from components.analytics import analytics
from components.home import home

st.set_page_config(layout="wide")

data = pd.read_csv('dataset/imdb_ratings.csv')

data = data.drop('Unnamed: 0', axis='columns')

if 'page' not in st.session_state:
    st.session_state.page = 'Home'

page = st.sidebar.selectbox(
    "☰ Navigation",
    ['Home', 'Analytics', 'About'],
    index=['Home', 'Analytics', 'About'].index(st.session_state.page)
)

st.session_state.page = page

if st.session_state.page == 'Analytics':
    analytics(data)
elif st.session_state.page == 'Home':
    home(data)







