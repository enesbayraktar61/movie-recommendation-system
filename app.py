import streamlit as st
import pickle
import pandas as pd

# Load saved files
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Convert dictionary back to dataframe
movies = pd.DataFrame(movies_dict)

# Recommendation function
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# App title
st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get 5 similar movie recommendations.")

# Movie selection
selected_movie = st.selectbox("Choose a movie", movies["title"].values)

# Recommendation button
if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")
    for movie in recommendations:
        st.write(movie)