# Content-Based Movie Recommendation System

This phase implements a content-based filtering recommendation engine using TF-IDF vectorization and cosine similarity. It suggests movies based on user input—either a movie title or a descriptive tag—and compares specific features such as genre, actor name, director name, or plot keywords.

## Dataset
 
 - updated_movies.csv: Contains detailed metadata about movies including title, genres, actors, director, plot keywords, and IMDb scores.

 - movies_tags.csv: Includes movie taglines used to assist tag-based search and recommendations.

## How It Works

1. User Input Options
Users can choose to:

  - Enter a movie title

  - Enter a tagline keyword (e.g., "space", "warrior") to find a related movie

2. Recommendation Methods
Once a movie is identified, users can choose from five recommendation strategies:

   1. Based on Genres

   2. Based on Actor Name

   3. Based on Director Name

   4. Based on Plot Keywords

   5. Display Top 5 Highest Rated Movies (based on IMDb scores)

3. TF-IDF & Cosine Similarity

 - Text data from the chosen feature is vectorized using TF-IDF.

 - Pairwise cosine similarity is calculated.

 - The top 15 most similar movies are identified and filtered using an IMDb score threshold (≥ 7.0).

4. Display & Filtering
 - Final recommendations are filtered and sorted by IMDb rating.

 - A table of top 10 relevant movies is displayed to the user.

5. Evaluation
A small test sample is used to evaluate the system's performance using: Precision ,Recall ,and F1 Score

