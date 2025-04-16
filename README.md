# Movie Recommendation System


A web-based movie recommendation system built with Flask and Python, using content-based filtering to recommend movies based on user input.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Recommendation Approach](#recommendation-approach)
- [Project Structure](#project-structure)
- [Results & Screenshots](#results--screenshots)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## About the Project
This Movie Recommendation System leverages content-based filtering to suggest movies based on the features of a movie that a user has already shown interest in. Using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity, the system compares movie attributes like genre, cast, director, and plot keywords to recommend similar titles.

## Features

- **Movie Search by Tag or Title**:  
  Users can input a tag (e.g., *"At the end of the world, the adventure begins."*) or a movie title (e.g., *"Pirates of the Caribbean: At World's End"*) to search for similar movies.

- **Content-Based Filtering**:  
  The system matches movies based on shared features such as genre, cast, director, and plot keywords.

- **Recommendation Ranking**:  
  Results are filtered and ranked based on IMDb scores, ensuring high-quality recommendations.

- **User Interface**:  
  The system uses Flask to render a simple web interface, displaying movie recommendations along with key details such as genre, cast, director, and plot overview.

## Tech Stack

## Dataset

This project uses multiple datasets to support both content-based and collaborative filtering techniques:

- [Movie Recommendations Dataset (Kaggle)](https://www.kaggle.com/datasets/sreenathkk/movie-recommendations)  
  *Used for content-based filtering.*  
  **Includes:** Director name, number of critic reviews, duration, genres, actor names, movie title, number of voted users, plot keywords, IMDb link, number of user reviews, language, country, year of release, IMDb score.

- [Movie Metadata Dataset (Kaggle)](https://www.kaggle.com/datasets/brtej1/movie-metadata-csv)  
  *Used for content-based filtering.*  
  *Used to retrieve movie titles based on taglines and to get the homepage of each movie.*  
  **Includes:** Genres, homepage, keywords, overview, runtime, tagline, title, cast, director.

- [MovieLens Dataset (GroupLens)](https://grouplens.org/datasets/movielens/)  
  *Used for collaborative filtering.*  
  *Utilized two datasets from this source:*  
  - **Movies dataset:** Contains movie titles, IDs, and genres.  
  - **Ratings dataset:** Contains movie IDs, ratings, and user IDs.


## Installation

## Usage

## Recommendation Approach

## Project Structure

## Results & Screenshots

## Future Improvements

## Contributing

## License
This project is licensed under the MIT License.
