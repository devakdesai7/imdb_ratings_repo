import streamlit as st
import pandas as pd
import numpy as np

def home(data):
    col1, col2 = st.columns(2)

    num_of_movies = len(list(data['title']))
    average_of_all_ratings = data['averageRating'].mean()

    with col1: 
        with st.container(border=True):
            st.markdown(
                "<h2 style='color: rgb(255, 47, 0)'>Movies Analysed: </h2>", unsafe_allow_html=True
            )
            st.markdown(
                f"""
                    <p style='font-size: 30px; color: rgb(255, 138, 110)'>
                        {num_of_movies}
                    </p>
                """, unsafe_allow_html = True
            )
    with col2:
        with st.container(border=True):
            st.markdown(
                "<h2 style='color: rgb(255, 47, 0)'>Average Rating: </h2>", unsafe_allow_html=True
            )
            st.markdown(
                f"""
                    <p style='font-size: 30px; color: rgb(255, 138, 110)'>
                        {average_of_all_ratings:.2f}
                    </p>
                """, unsafe_allow_html = True
            )
    
    st.text(
        """This dashboard takes a look at IMDb ratings for around 67,500 movies to understand how audiences respond to different films. It explores how average ratings are spread across movies and how those ratings connect with the number of votes each movie receives. Some movies are highly rated but have fewer votes, while others attract massive attention even with moderate ratings — and this dashboard helps surface those patterns.

By interacting with the visualizations, you can get a sense of what “popular” really means, spot trends in audience preferences, and see how movie quality and popularity relate to each other across a large and diverse collection of films."""
    )
    
    if st.button("See Analytics"):
        st.session_state.page = 'Analytics'
        st.rerun()
        