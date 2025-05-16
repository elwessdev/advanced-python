import streamlit as st
import requests
import json

st.title("Movie Explorer")

API_BASE_URL = "http://localhost:8000"

if 'current_movie' not in st.session_state:
    st.session_state.current_movie = None
if 'summary' not in st.session_state:
    st.session_state.summary = None

def get_random_movie():
    try:
        response = requests.get(f"{API_BASE_URL}/movies/random/")
        if response.status_code == 200:
            movie_data = response.json()
            st.session_state.current_movie = movie_data
            st.session_state.summary = None
            return True
        else:
            st.error(f"Error fetching movie: {response.status_code}")
            return False
    except Exception as e:
        st.error(f"Error connecting to API: {str(e)}")
        return False

def get_movie_summary(movie_id):
    try:
        payload = {"movie_id": movie_id}
        response = requests.post(
            f"{API_BASE_URL}/generate_summary/",
            json=payload
        )
        if response.status_code == 200:
            summary_data = response.json()
            st.session_state.summary = summary_data.get("summary_text")
            return True
        else:
            st.error(f"Error fetching summary: {response.status_code}")
            return False
    except Exception as e:
        st.error(f"Error connecting to API: {str(e)}")
        return False

st.header("Explore Movies")

if st.button("Show Random Movie"):
    get_random_movie()

if st.session_state.current_movie:
    movie = st.session_state.current_movie
    st.subheader(f"{movie['title']} ({movie['year']})")
    st.write(f"Director: {movie['director']}")
    
    st.write("Starring:")
    for actor in movie['actors']:
        st.write(f"• {actor['actor_name']}")

    if st.button("Get Summary"):
        get_movie_summary(movie['id'])

if st.session_state.summary:
    st.subheader("Movie Summary")
    st.info(st.session_state.summary)