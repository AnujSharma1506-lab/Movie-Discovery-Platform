import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c06446caae11657b9c3f29e94e1a62c5")
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w185/" +data['poster_path']

movies_dict=pickle.load(open('movies_dict.pkl' ,'rb'))
movies=pd.DataFrame(movies_dict)
movies_list=movies['title'].values
st.title('🎬 Movie Recommender system')
selected_movie_name=st.selectbox("Enter a movie you like:",movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))



def recommend(movie):
    movie_index=movies[movies['title'] == movie ].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    recommended_ids = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_ids.append(movie_id)
    return recommended_movies,recommended_movies_poster,recommended_ids

if st.button('Recommend'):
    names,posters,ids=recommend(selected_movie_name)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

