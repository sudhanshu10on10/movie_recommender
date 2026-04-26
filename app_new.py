import streamlit as st
import pickle
import pandas as pd
import requests

def fetchposter(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f191b676f7148fbb224a6c7190001c5c&language=en-US'
    )
    data = response.json()
    if 'poster_path' not in data or data['poster_path'] is None:
        return "https://via.placeholder.com/500"
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetchposter(movie_id))
    return recommended_movies, recommended_movies_posters

# Pickle Inputs
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

import gdown
import os

if not os.path.exists('movies_dict.pkl'):
    gdown.download('https://drive.google.com/file/d/1kPaH0pn4P6-3s50xTt_n1bsVDN-BrcKU/view?usp=sharing', 'movies_dict.pkl', quiet=False)

if not os.path.exists('similarity.pkl'):
    gdown.download('https://drive.google.com/file/d/1Gq4S0LaXLguMIdTpltN4Ftw-d5C2BpFO/view?usp=sharing', 'similarity.pkl', quiet=False)

# Website
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select a Movie',
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])