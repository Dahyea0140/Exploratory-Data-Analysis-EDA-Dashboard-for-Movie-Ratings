import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Top 10 Movies by Average Rating")

st.write(
    "This app displays the top 10 movies based on average ratings from the dataset."
)


@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv", index_col=0)
    movies = movies.loc[:, ~movies.columns.str.contains("^Unnamed")]

    # Display the first 5 rows of the DataFrame

    ratings = pd.read_csv("ratings.csv", index_col=0)
    ratings = ratings.loc[:, ~ratings.columns.str.contains("^Unnamed")]

    # Display the first 5 rows of the DataFrame

    movies_ratings = movies.merge(ratings, on="movieId", how="inner").dropna()

    movies_ratings = (
        movies_ratings.groupby(["movieId", "title"])["rating"]
        .agg(["mean", "count"])
        .reset_index()
    )

    movies_ratings = movies_ratings.rename(
        columns={"mean": "avg_rating", "count": "num_ratings"}
    )

    movies_ratings["avg_rating"] = movies_ratings["avg_rating"].round(2)

    reliable = movies_ratings[movies_ratings["num_ratings"] >= 100]

    top_rated = reliable.sort_values(by="avg_rating", ascending=False).reset_index(
        drop=True
    )

    return top_rated


top_rated = load_data()


st.write(
    "Data Loaded!",
    top_rated.shape[0],
    "ratings from",
    top_rated["title"].nunique(),
    "movies",
)

st.dataframe(top_rated.drop(columns=["movieId"]).head(10), hide_index=True)
