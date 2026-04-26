# Movie Recommender System with end-to-end deployment

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
- Dataset: TMDB 5000 Movies from Kaggle
- Download from: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Other Files
- Cosine Similarity Matrix - https://drive.google.com/file/d/1Gq4S0LaXLguMIdTpltN4Ftw-d5C2BpFO/view?usp=drive_link
- Movies Dictionary - https://drive.google.com/file/d/1kPaH0pn4P6-3s50xTt_n1bsVDN-BrcKU/view?usp=drive_link
