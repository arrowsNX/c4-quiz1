# feno01_project1.py

This project is a Python script designed to perform data cleaning, preprocessing, and exploratory analysis on a movie dataset. The code reads a CSV file (`movie_dataset.csv`), processes data, and calculates key statistics and insights, such as finding the highest-rated movie, average revenue, and identifying popular actors.

## Features

The script provides insights into the following aspects of the dataset:
1. **Highest-Rated Movie**: Identifies the movie with the highest rating.
2. **Average Revenue**: Calculates the average revenue across all movies and for a specified time range (2015–2017).
3. **Movies Released in 2016**: Counts the number of movies released in 2016.
4. **Christopher Nolan’s Movies**: Lists movies directed by Christopher Nolan and calculates the median rating of his movies.
5. **Highly Rated Movies**: Counts the number of movies with a rating of 8.0 or higher.
6. **Year with Highest Average Rating**: Finds the year with the highest average movie rating.
7. **Percentage Increase in Movies**: Calculates the percentage increase in the number of movies released from 2006 to 2016.
8. **Most Common Actor**: Identifies the actor who appears most frequently across all movies.
9. **Unique Genres**: Determines the number of unique genres in the dataset.

## Dataset

The code expects a CSV file named `movie_dataset.csv` with the following key columns:
- `Title`: Title of the movie
- `Rating`: IMDB rating of the movie
- `Revenue (Millions)`: Revenue of the movie in millions
- `Year`: Release year of the movie
- `Director`: Director of the movie
- `Actors`: Lead actors in the movie
- `Genre`: Genre(s) of the movie

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/arrowsNX/c4-quiz1.git
   cd c4-quiz1
   ```
2. **Install dependencies: The script requires pandas and numpy for data processing and analysis. Install them using:
   ```bash
   pip install pandas numpy
   ```

   
3. **Run the script: Ensure movie_dataset.csv is in the same directory, then execute the script:
 ```bash
python feno01_project1.py

```
## Usage

Run the script to view various statistics in the console. For example:

```plaintext

The highest rated movie is: Inception with a rating of 8.8
Average revenue of all movies: 90.2
Average revenue from 2015-2017: 100.4
Number of movies released in 2016: 45
Number of movies directed by Christopher Nolan: 7
```

## Error Handling

If `movie_dataset.csv` is not found, the script will display an error message:

```plaintext

Error: 'movie_dataset.csv' not found.
```

## Contributing

Feel free to fork this repository, submit issues, or create pull requests to contribute to this project.

### ps :
I have already made two updates.
1. `feno01_project1_update.py`
2. `feno01_project1_update2.py`

These versions are more interactive.
