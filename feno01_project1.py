#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:37:33 2024

@author: feno
"""


import pandas as pd


# Load the dataset
try:
    df = pd.read_csv("movie_dataset.csv")
except FileNotFoundError:
    print("Error: 'movie_dataset.csv' not found.")
    exit()

# Data Cleaning and Preprocessing
# ----------------------------------------------------------------
# Remove spaces from column names for easier access
df.columns = df.columns.str.replace(' ', '_')

# Handle missing values in specific columns by filling with mean
df['Revenue_(Millions)'] = df['Revenue_(Millions)'].fillna(df['Revenue_(Millions)'].mean())
df['Metascore'] = df['Metascore'].fillna(df['Metascore'].mean())

# Calculate statistics and insights
# ----------------------------------------------------------------

# 1. Finding the highest-rated movie
if 'Rating' in df.columns:
    highest_rated_movie = df.loc[df['Rating'].idxmax()]
    print('The highest rated movie is:', highest_rated_movie['Title'], 'with a rating of', highest_rated_movie['Rating'])

# 2. Average revenue of all movies in the dataset
average_revenue = df['Revenue_(Millions)'].mean()
print('Average revenue of all movies:', average_revenue)

# 3. Average revenue of movies from 2015 to 2017
data_15_17 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
avg_revenue_15_17 = data_15_17['Revenue_(Millions)'].mean()
print('Average revenue from 2015-2017:', avg_revenue_15_17)

# 4. Number of movies released in 2016
movies_count_2016 = df[df['Year'] == 2016].shape[0]
print('Number of movies released in 2016:', movies_count_2016)

# 5. Movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
nolan_movies_count = nolan_movies.shape[0]
print('Number of movies directed by Christopher Nolan:', nolan_movies_count)

# 6. Number of movies with a rating of at least 8.0
high_rating_movies_count = df[df['Rating'] >= 8.0].shape[0]
print('Number of movies with a rating of at least 8.0:', high_rating_movies_count)

# 7. Median rating of movies directed by Christopher Nolan
if not nolan_movies.empty:
    nolan_median_rating = nolan_movies['Rating'].median()
    print('Median rating of movies directed by Christopher Nolan:', nolan_median_rating)

# 8. Year with the highest average rating
year_avg_rating = df.groupby('Year')['Rating'].mean()
year_highest_avg_rating = year_avg_rating.idxmax()
print('Year with the highest average rating:', year_highest_avg_rating)

# 9. Percentage increase in the number of movies made between 2006 and 2016
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
if movies_2006 > 0:
    percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
    print('Percentage increase between 2006 and 2016:', percentage_increase)

# Additional Analyses
# ----------------------------------------------------------------

# 10. Finding the most common actor in all the movies
if 'Actors' in df.columns:
    actors_split = df['Actors'].str.split(r',\s*').explode()
    most_common_actor = actors_split.value_counts().idxmax()
    print('Most common actor in all the movies:', most_common_actor)

# 11. Number of unique genres in the dataset
if 'Genre' in df.columns:
    genres_split = df['Genre'].str.split(r',\s*').explode()
    unique_genres = genres_split.nunique()
    print('Number of unique genres in the dataset:', unique_genres)



"""The highest rated movie is: The Dark Knight with a rating of 9.0
Average revenue of all movies: 82.95637614678898
Average revenue from 2015-2017: 68.06402328198025
Number of movies released in 2016: 297
Number of movies directed by Christopher Nolan: 5
Number of movies with a rating of at least 8.0: 78
Median rating of movies directed by Christopher Nolan: 8.6
Year with the highest average rating: 2007
Percentage increase between 2006 and 2016: 575.0
Most common actor in all the movies: Mark Wahlberg
Number of unique genres in the dataset: 20"""