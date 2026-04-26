# Movie Recommender System

A content-based movie recommender system built with Python and Streamlit that suggests similar movies based on your selection.

## Live Demo
[Click here to try the app](https://movierecommender-za83gj3rmserf56vlixdcw.streamlit.app/)

## How It Works
- Uses **cosine similarity** on movie tags (genres, cast, crew, keywords)
- Fetches movie posters from the **TMDB API**
- Built with **Streamlit** for the frontend

## Tech Stack
- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn
- TMDB API

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dataset
Based on the TMDB 5000 Movies dataset from Kaggle.
