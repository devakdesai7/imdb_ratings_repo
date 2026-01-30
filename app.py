import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    "<h1 style='color:rgb(255, 47, 0); text-align:center; font-family:'Times New Roman';'>IMDb Ratings analysis for Movies that are publicly available</h1>",
    unsafe_allow_html=True
)

data = pd.read_csv('dataset/imdb_ratings.csv')

st.dataframe(data)

min_ratings, max_ratings = st.slider("Select ratings' range", 0, 10, (0, 5))
filtered = data[(data['averageRating'] >= min_ratings) & (data['averageRating'] <= max_ratings)]

fig = px.histogram(
    filtered, 
    x = "averageRating",
    labels = {
        'averageRating' : 'Average Rating',
        'count' : 'Number of Movies'
    },
    nbins = ((int(max_ratings - min_ratings)) * 2),
    title = 'Ratings distribution in the selected range of ratings'
)

fig.update_traces(
    marker_line_color = 'black',
    marker_line_width = 1,
    marker_color = '#FF2F00',
    opacity = 0.7 
)

fig.update_layout(
    shapes = [
        dict(
            type="rect",
            xref="x domain",
            yref="y domain",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line=dict(color="white", width=2)
        )
    ]
)

st.plotly_chart(fig)





