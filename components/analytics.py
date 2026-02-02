import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

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

def analytics(data):
    st.markdown(
    "<h1 style='color:rgb(255, 47, 0); text-align:center; font-family:'Times New Roman';'>IMDb Ratings analysis for Movies that are publicly available</h1>",
    unsafe_allow_html=True
    )
    st.divider()

    st.dataframe(data)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
        
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

            st.plotly_chart(fig, use_container_width=True)

    with col2:
        with st.container(border=True): 
            min_votes, max_votes = st.slider("Select ratings' range", 1, 1600000, (1, 1000000))

            required_df = data[(data['numVotes'] >= min_votes) & (data['numVotes'] <= max_votes)]
            required_df['log_scaled_numVotes'] = np.log10(required_df['numVotes'])

            num_votes_histogram = px.histogram(
                required_df,
                x=required_df['log_scaled_numVotes'],
                nbins = int(np.log10(max_votes)) - int(np.log10(min_votes)),
                title="Distribution of number of votes given to movies"
            )

            apply_basic_style_to_figure(num_votes_histogram)

            st.plotly_chart(num_votes_histogram, use_container_width=True)

    with st.container(border=True):
        scatterplot_of_ratings_votes = px.scatter(
            data,
            x=data['averageRating'],
            y=data['numVotes'],
            hover_name=data['title'],
            title='Distribution of movies based on the number of votes it got and it\'s average rating',
        )

        apply_basic_style_to_figure(scatterplot_of_ratings_votes)
        st.plotly_chart(scatterplot_of_ratings_votes, use_container_width=True)
        st.text(
            "The points having a higher number of votes along with a high rating are the box-office successes whereas the ones with high ratings and low number of votes are underrated gems and the ones with both of them low are box-office failures."
        )