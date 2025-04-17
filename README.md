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
- [Results & Screenshots](#results--screenshots)
- [Future Improvements](#future-improvements)
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

- **Language**: Python

- **Libraries**: Pandas, NumPy, Scikit-Learn, Flask

- **Web Framework** : Flask

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

Follow these steps to set up the project:

1. **Clone the repository**:
   ```bash
   https://github.com/jassyo/movie-recommendation-system.git
   cd /movie-recommendation-system
 2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

## Usage

1. **Run MRS.py:**

   Execute the script to start the Movie Recommendation System.
   ```bash
   python MRS.py

2. **Install NGROK:**

   If you don't have NGROK installed, you can download and install it from [here](https://ngrok.com/downloads/windows).

3. **Run NGROK:**

    After installing NGROK, open the command line or terminal and run the following command:
   ```bash
   ngrok http 5000

4. **Access the Web App**
   After running the command, NGROK will generate a public URL. Use the provided link to access the Movie Recommendation System. 

## Recommendation Approach
1.**Content-Based Filtering (TF-IDF):**
This section uses TF-IDF Vectorization and Cosine Similarity to recommend movies based on a movie title or tag entered by the user.

2.**Collaborative Filtering (User-Item Matrix):**
a K-Nearest Neighbors (KNN) algorithm is used for collaborative filtering based on user ratings. We use a sparse matrix to represent the user-item interactions, and then find similar users to recommend movies.


## Results & Screenshots


![Movie Recommendation System](https://github.com/user-attachments/assets/bf25baff-4b6c-4140-898f-03ae5692a2b2)



## Future Improvements
 - 	Incorporate Item-Based Collaborative Filtering
 - 	Address the Cold Start Problem
 - 	Explore Hybrid Approaches blending both filtering methods
 - 	Migrate to scalable frameworks like LightFM or Surprise
 - 	Hybrid Recommendation System: Merging content-based and collaborative outputs could improve robustness.
 - 	Cold Start Solutions: Consider integrating user registration and preference capturing at first interaction.
 - 	Performance Scaling: Move to more scalable libraries or GPU-based models for real-time recommendations.
 - 	User Feedback Loop: Include feedback features to retrain models with evolving user preferences.


## License
This project is licensed under the MIT License.
