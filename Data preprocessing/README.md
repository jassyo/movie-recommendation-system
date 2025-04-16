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
 
2. Text Cleanup
      - Cleaned up non-standard characters in movie titles (e.g., weird trailing symbols like Â).

      - Converted genre strings to lowercase and split them into lists.

      - Converted plot keywords into lowercase and replaced separators.
3. Handling Missing Values:
      - Checked for missing values across all relevant fields.

      - Fetched missing values using the OMDb API for: director_name ,title_year ,plot_keywords ,language ,country
      
      - Added a delay (sleep(1)) between API requests to respect rate limits.

4.  Filling Remaining Nulls
      
      - Filled numeric columns (num_critic_for_reviews, duration, etc.) using column means.
      
      - Filled categorical columns using the mode (most frequent value).

      - Dropped remaining rows with null values in plot_keywords (critical for later NLP tasks).

## Output
The final cleaned and enriched dataset is saved as: updated_movies.csv

##  Tools & Libraries Used
  1. pandas: For data loading, manipulation, and cleanup.

  2. requests: To interact with the OMDb API.

  3. csv: For custom parsing of non-standard CSV content.

  4. time: To manage API request rate with sleep delays.

## API Used:
MDb API: Used to fetch movie metadata such as director, year, plot, language, and country.
API Key Used: 3c45df53 (Replace with your own for production or shared projects)

