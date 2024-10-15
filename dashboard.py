import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
df = pd.read_csv('omdb_top_movies.csv')

# Example Rotten Tomatoes data
rt_data = {
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', '12 Angry Men', 'Schindler\'s List',
              'Pulp Fiction', 'The Lord of the Rings: The Return of the King', 'The Good, the Bad and the Ugly',
              'Fight Club', 'Forrest Gump'],
    'RT_Rating': [91, 98, 94, 100, 97, 92, 95, 97, 79, 71]
}
rt_df = pd.DataFrame(rt_data)

# Merge IMDb and Rotten Tomatoes data on the movie title
combined_df = pd.merge(df, rt_df, on='Title', how='inner')

# Dashboard layout
st.title('Movie Ratings Comparison Dashboard')

st.header('Top 10 Movies by IMDb Rating')
st.write(combined_df[['Title', 'Rating', 'RT_Rating']].sort_values(by='Rating', ascending=False).head(10))

st.header('Comparison of IMDb and Rotten Tomatoes Ratings')
fig, ax = plt.subplots()
ax.scatter(combined_df['Rating'].astype(float), combined_df['RT_Rating'].astype(float), alpha=0.5)
ax.set_xlabel('IMDb Rating')
ax.set_ylabel('Rotten Tomatoes Rating')
ax.set_title('Comparison of IMDb and Rotten Tomatoes Ratings')
st.pyplot(fig)

st.header('Distribution of IMDb Ratings')
fig, ax = plt.subplots()
ax.hist(combined_df['Rating'], bins=20, edgecolor='k')
ax.set_xlabel('Rating')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of IMDb Ratings')
st.pyplot(fig)
