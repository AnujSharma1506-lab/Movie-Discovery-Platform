import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

TMDB_API_KEY = "c06446caae11657b9c3f29e94e1a62c5"  # Replace with your TMDB API key

def fetch_movie_info(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        'title': data.get('title', ''),
        'overview': data.get('overview', 'No overview'),
        'release_date': data.get('release_date', 'N/A'),
        'genres': [g['name'] for g in data.get('genres', [])],
        'rating': data.get('vote_average', 'N/A'),
        'poster_url': f"https://image.tmdb.org/t/p/w342/{data.get('poster_path', '')}"
    }

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None

def recommend(movie_title):
    idx = movies[movies['title'] == movie_title].index[0]
    distances = similarity[idx]
    top_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i[0]].id for i in top_indices]

st.title("🎬 Movie Recommender System")
selected_movie = st.selectbox("Enter a movie you like:", movies['title'].values)

if st.button("Recommend"):
    rec_ids = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for i, movie_id in enumerate(rec_ids):
        info = fetch_movie_info(movie_id)

        # Add clickable poster using custom HTML
        st.markdown(
            f"""
            <div style="display:inline-block; text-align:center; margin:10px;">
                <form action="" method="post">
                    <input type="hidden" name="clicked_id" value="{movie_id}">
                    <button type="submit" style="border:none; background:none;">
                        <img src="{info['poster_url']}" width="150"><br>
                        <span style="color:white;">{info['title']}</span>
                    </button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )

# Detect click using form POST
clicked_id = st.query_params.get("clicked_id", [None])[0]

if clicked_id:
    st.session_state.selected_movie_id = int(clicked_id)

# Show details
if st.session_state.selected_movie_id:
    movie = fetch_movie_info(st.session_state.selected_movie_id)
    st.markdown("---")
    st.header(movie['title'])
    st.image(movie['poster_url'], width=300)
    st.markdown(f"**📝 Overview:** {movie['overview']}")
    st.markdown(f"**📅 Release Date:** {movie['release_date']}")
    st.markdown(f"**🎭 Genres:** {', '.join(movie['genres'])}")
    st.markdown(f"**⭐ Rating:** {movie['rating']}/10")
