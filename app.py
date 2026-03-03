import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key=4ffd557cb3d3b0f7e9bd049545fd7c2d&language=en-US"
    data = requests.get(url).json()

    if data.get('poster_path'):
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

movies_dict = pickle.load(open('movie_list_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
<<<<<<< HEAD
similarity = pickle.load(open('similarity.pkl','rb'))
=======
top_similar = pickle.load(open('similarity.pkl','rb'))
>>>>>>> 82890a6 (fixed app.py after merge)

st.title("Movie Recommendation System")


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
<<<<<<< HEAD
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )
=======

    distances = top_similar[index]
>>>>>>> 82890a6 (fixed app.py after merge)

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:7]:
<<<<<<< HEAD
        movie_id = movies.iloc[i[0]]['id']
        recommended_movie_posters.append(fetch_poster(movie_id))  # FIXED
        recommended_movie_names.append(movies.iloc[i[0]]['title'])
=======

        # If tuple → take first element
        if isinstance(i, (list, tuple)):
            movie_index = int(i[0])
        else:
            movie_index = int(i)

        movie_id = movies.iloc[movie_index]['id']

        recommended_movie_names.append(
            movies.iloc[movie_index]['title']
        )

        recommended_movie_posters.append(
            fetch_poster(movie_id)
        )
>>>>>>> 82890a6 (fixed app.py after merge)

    return recommended_movie_names, recommended_movie_posters


selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values,
    index=None,
    placeholder="Choose intrested movie 😁"
)


if st.button('Show Similar Movies 🍿', type='primary'):

    if selected_movie_name is not None:

        with st.spinner("Finding similar movies..."):
            names, posters = recommend(selected_movie_name)

<<<<<<< HEAD
        # 🔥 Top Padding
=======
        # Top Padding
>>>>>>> 82890a6 (fixed app.py after merge)
        st.markdown("<div style='margin-top:60px;'></div>", unsafe_allow_html=True)

        # Wider center area (~85%)
        left_space, center, right_space = st.columns([1, 8, 1])

        with center:

            cols = st.columns(3, gap="large")

            for i in range(len(names)):
                with cols[i % 3]:
                    st.image(
                        posters[i],
                        width=300
                    )
                    st.markdown(
                        f"<div style='text-align:center; font-size:18px; font-weight:600; margin-top:10px;'>{names[i]}</div>",
                        unsafe_allow_html=True
                    )

<<<<<<< HEAD
        # 🔥 Bottom Padding
=======
        # Bottom Padding
>>>>>>> 82890a6 (fixed app.py after merge)
        st.markdown("<div style='margin-bottom:80px;'></div>", unsafe_allow_html=True)

    else:
        st.warning("Please select a movie first 😅")

