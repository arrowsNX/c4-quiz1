#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:34:27 2024
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
    print("3. Average revenue of movies for a specific date range")
    print("4. Number of movies released in a specific year")
    print("5. Number of movies directed by a specific director")
    print("6. Number of movies with a rating of at least 8.0")
    print("7. Median rating of movies directed by a specific director")
    print("8. Year with the highest average rating")
    print("9. Percentage increase in the number of movies between two specific years")
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
        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))
        data_range = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
        avg_revenue = data_range['Revenue_(Millions)'].mean()
        print(f'Average revenue from {start_year} to {end_year}:', avg_revenue)

    elif choice == '4':
        year = int(input("Enter the year: "))
        movies_count = df[df['Year'] == year].shape[0]
        print(f'Number of movies released in {year}:', movies_count)

    elif choice == '5':
        director = input("Enter the director's name: ")
        director_movies_count = df[df['Director'] == director].shape[0]
        print(f'Number of movies directed by {director}:', director_movies_count)

    elif choice == '6':
        high_rating_movies_count = df[df['Rating'] >= 8.0].shape[0]
        print('Number of movies with a rating of at least 8.0:', high_rating_movies_count)

    elif choice == '7':
        director = input("Enter the director's name: ")
        director_movies = df[df['Director'] == director]
        if not director_movies.empty:
            director_median_rating = director_movies['Rating'].median()
            print(f'Median rating of movies directed by {director}:', director_median_rating)
        else:
            print(f"No movies found for director {director}.")

    elif choice == '8':
        year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()
        print('Year with the highest average rating:', year_highest_avg_rating)

    elif choice == '9':
        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))
        movies_start_year = df[df['Year'] == start_year].shape[0]
        movies_end_year = df[df['Year'] == end_year].shape[0]
        if movies_start_year > 0:
            percentage_increase = ((movies_end_year - movies_start_year) / movies_start_year) * 100
            print(f'Percentage increase in the number of movies between {start_year} and {end_year}:', percentage_increase)
        else:
            print(f"No movies found in {start_year} for comparison.")

    elif choice == '10':
        actor = input("Enter the actor's name (or press Enter to find the most common actor): ")
        if actor:
            actor_count = df['Actors'].str.contains(actor, case=False, na=False).sum()
            print(f'Number of movies featuring {actor}:', actor_count)
        else:
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
