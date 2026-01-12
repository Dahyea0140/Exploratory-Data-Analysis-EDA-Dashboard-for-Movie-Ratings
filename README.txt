🎬 Exploratory Data Analysis (EDA) Dashboard for Movie Ratings

An interactive Streamlit dashboard that performs exploratory data analysis on the MovieLens movie ratings dataset.
The application helps users explore top-rated movies based on reliable average ratings and visualize insights from real-world data.

📌 Project Overview

This project focuses on analyzing movie ratings data and presenting insights through an interactive web dashboard.
The dashboard computes average ratings, filters movies based on minimum number of ratings, and displays the top-rated movies in both tabular and visual formats.

The goal of this project is to demonstrate:

Data cleaning and preprocessing

Aggregation and statistical analysis

Data visualization

Building interactive data applications using Streamlit

🚀 Features

Load and clean MovieLens datasets (movies.csv, ratings.csv)

Remove unnecessary index (Unnamed) columns

Merge movie metadata with user ratings

Calculate:

Average rating per movie

Total number of ratings per movie

Filter movies based on minimum rating count for reliability

Display:

Top-rated movies table

Horizontal bar chart of top 10 movies

Caching for improved performance

🛠️ Tech Stack

Python

pandas – data manipulation and aggregation

matplotlib – data visualization

Streamlit – interactive dashboard framework

📊 Dataset

The project uses the MovieLens dataset, a widely used dataset for recommender systems and data analysis.

movies.csv – movie metadata (title, genres)

ratings.csv – user ratings

Dataset source:
https://grouplens.org/datasets/movielens/

📂 Project Structure
Exploratory-Data-Analysis-EDA-Dashboard-for-Movie-Ratings/
│
├── app.py               # Main Streamlit application
├── movies.csv           # Movie metadata
├── ratings.csv          # Ratings data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

▶️ How to Run the App

Clone the repository:

git clone https://github.com/Dahyea0140/Exploratory-Data-Analysis-EDA-Dashboard-for-Movie-Ratings.git


Navigate to the project directory:

cd Exploratory-Data-Analysis-EDA-Dashboard-for-Movie-Ratings


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

📈 Example Insight

The dashboard highlights movies that have:

High average ratings

A sufficient number of ratings (to avoid bias from small samples)

This ensures that rankings are statistically meaningful, not just highly rated by a few users.

🧠 What I Learned

Handling real-world datasets with inconsistent indices

Difference between DataFrame index vs columns

Grouping and aggregating data using pandas

Importance of filtering data for reliability

Building and deploying interactive dashboards

Visualizing ranked data effectively using bar charts

🔮 Future Improvements

Add genre-based filtering

Add rating distribution visualizations

Include time-based rating trends

Add user-controlled sliders for minimum rating count

Deploy the app on Streamlit Cloud

📬 Contact

If you have suggestions or feedback, feel free to connect!
