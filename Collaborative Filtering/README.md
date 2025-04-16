#  Collaborative Filtering with User-Item Matrix


This project implements a User-Based Collaborative Filtering recommendation system using the K-Nearest Neighbors (KNN) algorithm. 
It recommends movies to users based on the preferences of similar users by leveraging a user-item rating matrix.

## Project Structure
**This notebook/script covers** : 

Loading and preprocessing movie rating datasets

 - Creating a user-item sparse matrix

 - Training a KNN model with cosine similarity

 - Generating movie recommendations for a given user

 - Evaluating recommendations using the Precision@k metric for different KNN n_neighbors values

##  Datasets
**The project uses two CSV files** :

 - movies.csv: Contains movieId and title

 - ratings.csv: Contains userId, movieId, and rating

## How It Works
 **1. Data Preparation:**

   - Merge movie titles with ratings.

   - Split the data into training and testing sets.

 **2. Matrix Creation:**

   - Map users and movies to unique indices.

   - Construct a sparse matrix of user-item interactions.

 **3. Model Training:**

   - Use sklearn.neighbors.NearestNeighbors with cosine similarity to find similar users.

 **4. Recommendation Function:**

   - For a given user, retrieve the top-N most similar users.

   - Recommend movies those users rated highly that the input user hasn’t seen.

 **5. Evaluation:**

   - Evaluate performance using Precision@5 for multiple k values (number of neighbors).

   - Display top recommended movie titles.
