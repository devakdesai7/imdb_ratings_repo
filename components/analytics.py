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

            myCol1, myCol2, myCol3 = st.columns([0.1, 3, 0.1])

            with myCol2:
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

            column1, column2, column3 = st.columns([0.1, 3, 0.1])

            with column2:
                st.plotly_chart(num_votes_histogram, width='content')

    with st.container(border=True):
        scatterplot_of_ratings_votes = px.scatter(
            data,
            x=data['averageRating'],
            y=data['numVotes'],
            hover_name=data['title'],
            title='Distribution of movies based on the number of votes it got and it\'s average rating',
        )

        apply_basic_style_to_figure(scatterplot_of_ratings_votes)
        cols1, cols2, cols3 = st.columns([0.5, 2, 0.5])
        with cols2:
            st.plotly_chart(scatterplot_of_ratings_votes, use_container_width=True)

        st.text(
            "The points having a higher number of votes along with a high rating are the box-office successes whereas the ones with high ratings and low number of votes are underrated gems and the ones with both of them low are box-office failures."
        )

    significant_movies_df = data[data['numVotes'] > 10000]
    

    with st.container(border=True):
        st.text("The following plot shows the plot of average ratings of movies having more than 10000 votes, this is necessary because there are many movies with very less votes that are flunking the data with no significance of their ratings at all.")

        myCols1, myCols2, myCols3 = st.columns([0.5, 2, 0.5])

        with myCols2:
            min_significant_votes, max_significant_votes = st.slider("Select the rating range for which you want to see the plot", 0, 10, (0, 5))

        required_significant_df = significant_movies_df[(significant_movies_df['averageRating'] >= min_significant_votes) & (significant_movies_df['averageRating'] <= max_significant_votes)]
        
        significant_movies_rating_histogram = px.histogram(
            required_significant_df,
            x = 'averageRating',
            nbins = (int(max_significant_votes - min_significant_votes)) * 2,
            labels={'averageRating' : 'Average Rating'},
            title='Distribution of movies having more than 10000 votes on the basis of its average ratings')
        
        apply_basic_style_to_figure(significant_movies_rating_histogram)

        col1, col2, col3 = st.columns([0.5, 2, 0.5])

        with col2:
            st.plotly_chart(significant_movies_rating_histogram, width='stretch')

    