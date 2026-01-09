import pandas as pd
import matplotlib.pyplot as plt

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
    drop=False
)
print(top_rated.head())

top_10 = top_rated.head(10)

plt.barh(top_10["title"], top_10["avg_rating"])
plt.title("Top 10 Movies by Average Rating (with at least 100 ratings)")
plt.xlabel("Movie Rating")
plt.ylabel("Movie Title")
plt.gca().invert_yaxis()
plt.show()
