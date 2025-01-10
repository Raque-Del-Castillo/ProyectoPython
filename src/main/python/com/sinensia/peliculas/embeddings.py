import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def carga_datos(filepath):
    """
    Se cargan los datos del archivo CSV + Conversion de embeddings a arrays de numpy para su procesamiento.
    """
    movies = pd.read_csv(filepath)
    movies['embedding'] = movies['embedding'].apply(lambda x: np.fromstring(x.strip('[]'),sep=','))
    return movies

def calculo_similar_coseno(embeddings, target_embedding):
    """
    Se calcula la similitud coseno existente entre el embedding objetivo y el resto
    """
    return cosine_similarity([target_embedding], embeddings).flatten()

def detalles_pelicula(movie):
    """
    Se muestran los detalles de la pelicula
    """
    st.write(f"Pelicula: {movie['title']}")
    st.write(f"Resumen: {movie['overview']}")
    st.write(f"Generos: {movie['genres']}")

def display_similar_movies(movies):
    """
    Se muestran las peliculas similares 
    """
    st.write("Peliculas similares")
    for _, row in movies.iterrows():
        st.write(f"Titulo: {row['title']}")
        st.write(f"Resumen: {row['overview']}")

def main():
    """
    La generacion de embeddings no he conseguido ponerla en funcionamiento, pero asi no explota
    """
    filepath = 'combined_info_movies_partial_with_embeddings.csv.csv'
    movies = carga_datos(filepath)

    movie_titles = movies['title'].tolist()

    input_movie = st.sidebar.selectbox("Selecciona una pelicula que te haya gustado", movie_titles)

    if input_movie:
        input_movie_row = movies[movies['title'] == input_movie].iloc[0]
        detalles_pelicula(input_movie_row)

        target_embedding = input_movie_row['embedding']

        embeddings = np.vstack(movies['embedding'].values)
        similaridad = cosine_similarity([target_embedding], embeddings).flatten()

        movies_copy = movies.copy()

        movies_copy = movies_copy.assign(similaridad.similarities)
        movies_copy = movies_copy[movies_copy['title'] != input_movie]
        similar_movies = movies_copy.sort_values(by = 'similaridad', ascending = False).head(10)

        display_similar_movies(similar_movies)

if __name__ == "__main__":
    main()

        
