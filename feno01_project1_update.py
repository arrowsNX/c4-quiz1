#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:06:05 2024

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
df.columns = df.columns.str.replace(' ', '_')
df['Revenue_(Millions)'] = df['Revenue_(Millions)'].fillna(df['Revenue_(Millions)'].mean())
df['Metascore'] = df['Metascore'].fillna(df['Metascore'].mean())

# Interactive Menu
# ----------------------------------------------------------------
def menu():
    print("\nChoose an option to analyze the movie dataset:")
    print("1. Find the highest rated movie")
    print("2. Average revenue of all movies")
    print("3. Average revenue of movies from 2015 to 2017")
    print("4. Number of movies released in 2016")
    print("5. Number of movies directed by Christopher Nolan")
    print("6. Number of movies with a rating of at least 8.0")
    print("7. Median rating of movies directed by Christopher Nolan")
    print("8. Year with the highest average rating")
    print("9. Percentage increase in the number of movies made between 2006 and 2016")
    print("10. Find the most common actor in all movies")
    print("11. Number of unique genres in the dataset")
    print("12. Exit")

def execute_choice(choice):
    if choice == '1':
        highest_rated_movie = df.loc[df['Rating'].idxmax()]
        print('The highest rated movie is:', highest_rated_movie['Title'], 'with a rating of', highest_rated_movie['Rating'])
    elif choice == '2':
        average_revenue = df['Revenue_(Millions)'].mean()
        print('Average revenue of all movies:', average_revenue)
    elif choice == '3':
        data_15_17 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
        avg_revenue_15_17 = data_15_17['Revenue_(Millions)'].mean()
        print('Average revenue from 2015-2017:', avg_revenue_15_17)
    elif choice == '4':
        movies_count_2016 = df[df['Year'] == 2016].shape[0]
        print('Number of movies released in 2016:', movies_count_2016)
    elif choice == '5':
        nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]
        print('Number of movies directed by Christopher Nolan:', nolan_movies_count)
    elif choice == '6':
        high_rating_movies_count = df[df['Rating'] >= 8.0].shape[0]
        print('Number of movies with a rating of at least 8.0:', high_rating_movies_count)
    elif choice == '7':
        nolan_median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
        print('Median rating of movies directed by Christopher Nolan:', nolan_median_rating)
    elif choice == '8':
        year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()
        print('Year with the highest average rating:', year_highest_avg_rating)
    elif choice == '9':
        movies_2006 = df[df['Year'] == 2006].shape[0]
        movies_2016 = df[df['Year'] == 2016].shape[0]
        if movies_2006 > 0:
            percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
            print('Percentage increase between 2006 and 2016:', percentage_increase)
    elif choice == '10':
        actors_split = df['Actors'].str.split(r',\s*').explode()
        most_common_actor = actors_split.value_counts().idxmax()
        print('Most common actor in all the movies:', most_common_actor)
    elif choice == '11':
        genres_split = df['Genre'].str.split(r',\s*').explode()
        unique_genres = genres_split.nunique()
        print('Number of unique genres in the dataset:', unique_genres)
    elif choice == '12':
        print("Exiting. Thank you!")
        exit()
    else:
        print("Invalid choice, please try again.")

# Main Loop
# ----------------------------------------------------------------
while True:
    menu()
    user_choice = input("Enter the number of your choice: ")
    execute_choice(user_choice)
