import streamlit as st
import pandas as pd

from components.analytics import analytics
from components.home import home

st.set_page_config(layout="wide")

data = pd.read_csv('dataset/imdb_ratings.csv')

data = data.drop('Unnamed: 0', axis='columns')

page = st.sidebar.selectbox(
    "☰ Navigation",
    ['Home', 'Analytics', 'About']
)

if page == 'Analytics':
    analytics(data)
elif page == 'Home':
    home(data)







