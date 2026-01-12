import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Top 10 Movies by Average Rating")

st.write(
    "This app displays the top 10 movies based on average ratings from the dataset."
)


# Load and preprocess data
@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv", index_col=0)
    movies = movies.loc[:, ~movies.columns.str.contains("^Unnamed")]

    # Display the first 5 rows of the DataFrame

    ratings = pd.read_csv("ratings.csv", index_col=0)
    ratings = ratings.loc[:, ~ratings.columns.str.contains("^Unnamed")]

    # Display the first 5 rows of the DataFrame

    movies_ratings = movies.merge(ratings, on="movieId", how="inner").dropna()

    # Calculate average ratings and number of ratings per movie
    movies_ratings = (
        movies_ratings.groupby(["movieId", "title"])["rating"]
        .agg(["mean", "count"])
        .reset_index()
    )

    # Rename columns for clarity
    movies_ratings = movies_ratings.rename(
        columns={"mean": "avg_rating", "count": "num_ratings"}
    )

    # Round average ratings to 2 decimal places
    movies_ratings["avg_rating"] = movies_ratings["avg_rating"].round(2)

    # Filter movies with at least 100 ratings for reliability
    reliable = movies_ratings[movies_ratings["num_ratings"] >= 100]

    # Sort movies by average rating in descending order
    top_rated = reliable.sort_values(by="avg_rating", ascending=False).reset_index(
        drop=True
    )

    return top_rated


top_rated = load_data()

# Sidebar for filtering
min_ratings = st.slider(
    "Minimum number of ratings",
    1,
    500,
    100,
    key="min_ratings",
    help="Select the minimum number of ratings a movie must have to be considered.",
)


filtered = top_rated[top_rated["num_ratings"] >= min_ratings]

top_movies = filtered.sort_values(by="avg_rating", ascending=False).head(10)

st.dataframe(
    top_movies.drop(columns=["movieId"]), use_container_width=True, hide_index=True
)

# Visualization

st.write("### Top 10 Movies Bar Chart")
fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(top_movies["title"][::-1], top_movies["avg_rating"][::-1], color="skyblue")
ax.set_xlabel("Average Rating")
ax.set_title("Top 10 Movies")
st.pyplot(fig)
