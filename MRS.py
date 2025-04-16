from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__, template_folder='D:\\summer training\\shabab\\project\\templates')


df = pd.read_csv("D:\\summer training\\shabab\\project\\datasets after cleaning\\updated_movies dataset.csv")
df_tags = pd.read_csv("D:\\summer training\\shabab\\project\\movies_tags.csv")

print(df.columns)  # Ensure 'genres' is present here
print(df_tags.columns)  # Ensure 'genres' is not expected here


def find_movie_from_tag(tag):
    tag = tag.strip().lower()
    matched_movies = df_tags[df_tags['tagline'].str.contains(tag, case=False, na=False)]
    return matched_movies.iloc[0]['title'] if not matched_movies.empty else None


def find_movie_feature(movie_title, feature):
    movie_title = movie_title.strip().lower()
    movie_row = df[df["movie_title"].str.lower() == movie_title]
    return movie_row.iloc[0][feature] if not movie_row.empty else None


def fetch_recommendations(feature_data, query_value):
    idx = df[df[feature_data.name].str.contains(query_value, case=False, na=False)].index
    if len(idx) == 0:
        return []
    idx = idx[0]
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(feature_data.fillna(""))
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:16]
    return [i[0] for i in sim_scores]


def apply_filters(movie_indices):
    return df.iloc[movie_indices].sort_values(by="imdb_score", ascending=False).head(10)


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    error = None

    if request.method == 'POST':
        user_input = request.form.get('input_value', '').strip().lower()
        input_type = request.form.get('input_type')
        feature = request.form.get('feature')

        if input_type == 'tag':
            user_input = find_movie_from_tag(user_input)
            if not user_input:
                error = "Tag not found."
                return render_template('index.html', recommendations=[], error=error)

        feature_value = find_movie_feature(user_input, feature)
        if feature_value:
            movie_indices = fetch_recommendations(df[feature], feature_value)
            recommendations = apply_filters(movie_indices).to_dict(orient='records')

            # Merge recommendation data with the df_tags data
            recommendations_df = pd.DataFrame(recommendations)

            # Merge with df_tags on 'movie_title' and 'title'
            merged = recommendations_df.merge(df_tags, left_on='movie_title', right_on='title', how='left',
                                              suffixes=('_movie', '_tag'))

            # Merge with df to include genres and other movie details
            merged = merged.merge(df[['movie_title', 'genres']], on='movie_title', how='left')

            # Leave missing values as empty (do not fill with N/A)
            merged = merged.dropna(subset=['genres', 'homepage', 'tagline', 'cast', 'overview'])

            # Columns to display in the table
            columns_to_display = [
                'movie_title', 'genres', 'homepage', 'tagline', 'cast', 'overview',
                'director_name', 'duration', 'actor_1_name', 'num_voted_users',
                'plot_keywords', 'movie_imdb_link', 'language', 'country',
                'title_year', 'imdb_score'
            ]
            recommendations = merged[columns_to_display].to_dict(orient='records')
        else:
            error = "Movie not found."

    return render_template('index.html', recommendations=recommendations, error=error)


if __name__ == '__main__':
    app.run(debug=True)
