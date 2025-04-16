# Movie Metadata Preprocessing


This phase focuses on cleaning and preprocessing movie metadata using Python and external APIs  complete missing information.

## *Datasets Used*
- movie_metadata.csv: Original dataset containing raw metadata of movies.(Kaggle)](https://www.kaggle.com/datasets/sreenathkk/movie-recommendations)  

## *Main Objectives*
- Remove irrelevant or redundant columns.

- Handle missing values using the OMDb API.

- Normalize text-based columns (e.g., genres, plot keywords).

- Save a clean and enriched dataset for further use.


##  *Data Cleaning Steps*:
  1.  Initial Exploration
      - Loaded datasets using pandas.

      - Displayed shape and statistical summary of the main dataset (df1).

      - Identified and dropped irrelevant columns like social media likes, budget, gross, etc.
