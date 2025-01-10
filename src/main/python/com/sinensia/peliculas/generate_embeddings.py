import pandas as pd
import json
import openai

def load_data():
    credits = pd.read_csv('data/TMDB_5000_Movie/tmdb_5000_credits.csv')
    movies = pd.read_csv('data/TMDB_5000_Movie/tmdb_5000_movies.csv')

    links = pd.read_csv('data/TMDB_5000_movie/links.csv')
    links = links.drop(columns=['movieId'])

    credits = credits.rename(columns = {'title': 'credits_title', 'crew': 'credits_crew'})
    credits = credits.drop(columns=['credits_title'])

    movies = movies.merge(credits, left_on='id', right_on='movie_id', how='left')
    movies = movies.drop(columns=['credits_crew'])

    movies['cast'] = movies['cast'].apply(lambda x: json.loads(x))
    movies['cast'] = movies['cast'].apply(lambda x: {actor['name'] for actor in x})
    movies['cast'] = movies['cast'].apply(lambda x: ",".join(x))

    movies['genres'] = movies['genres'].apply(lambda x: json.loads(x))
    movies['genres'] = movies['genres'].apply(lambda x: {genre['name'] for genre in x})
    movies['genres'] = movies['genres'].apply(lambda x: ",".join(x))

    movies['keywords'] = movies['keywords'].apply(lambda x: json.loads(x))
    movies['keywords'] = movies['keywords'].apply(lambda x: {keyword['name'] for keyword in x})
    movies['keywords'] = movies['keywords'].apply(lambda x: ",".join(x))

    movies['combined_info'] = movies['title'] + ' ' + movies['cast'] + ' ' + movies['genres']+ ' ' + movies['keywords']

    return movies

def combine_info(movies):
    movies["combined_info"] = movies.apply(lambda row: f"{row['title']}. {row['overview']} Genres: {row['genres']}", axis=1)
    return movies['combined_info']

def create_embeddings(texts):
    response = openai.Embedding.create(input=texts, model = "text-embedding-ada-002")
    return response ['data'][0]['embedding']

movies = load_data()
movies_partial = movies.loc[:500].copy()
df = combine_info(movies_partial)

movies_partial["embedding"] = movies_partial["combined_info"].apply(create_embeddings)

movies_partial.to_csv('combined_info_movies_partial_with_embeddings.csv', index = False)
