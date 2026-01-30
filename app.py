import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def apply_basic_style_to_figure(fig):
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

    return fig

page = st.sidebar.selectbox(
    "☰ Navigation",
    ['Home', 'Analytics', 'About']
)

if page == 'Analytics':
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

    fig.update_yaxes(title_text="Number of Movies")
    apply_basic_style_to_figure(fig)

    st.plotly_chart(fig)


    with st.form("my_form"):
        min_votes = st.number_input("How much votes should a movie have atleast to be included in the distribution?: ", min_value=1, max_value=1600000, value=1)
        max_votes = st.number_input("How much votes should a movie have atmost to be included in the distribution?: ", min_value=1, max_value=1600000, value=1000000)
        submitted = st.form_submit_button("Submit Values")

    required_df = data[(data['numVotes'] >= min_votes) & (data['numVotes'] <= max_votes)]
    required_df['log_scaled_numVotes'] = np.log10(required_df['numVotes'])

    num_votes_histogram = px.histogram(
        required_df,
        x=required_df['log_scaled_numVotes'],
        nbins = int(np.log10(max_votes)) - int(np.log10(min_votes)),
        title="Distribution of number of votes given to movies"
    )

    apply_basic_style_to_figure(num_votes_histogram)

    st.plotly_chart(num_votes_histogram)








