import streamlit as st
import requests
from typing import Dict
from streamlit_lottie import st_lottie

def reccom():

    page_bg_img = '''
     <style>
     body {
     background-image: url("https://cdn.wallpaper.tn/large/Naruto-Minato-Wallpaper-4K-4385.jpg");
     background-size: cover;
     }
     </style>
     '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.sidebar.header("Welcome to Aniway🐼", anchor='', divider='red')
    st.sidebar.image(image="https://cdn.wallpapersafari.com/34/31/uYXCjx.jpg", use_column_width=True)
    

    st.title("Aniway: An animation Recommendation System 🦋🐼")
    st.subheader('', divider='red')
    st.header("Aniway: For All things animation!")
    st.divider()
    title_input = st.text_input("Enter an anime title:")
    if st.button("Suggest!!"):
        recommendation = get_recommendations(title_input)
        st.write("Recommended Movies:")
        if isinstance(recommendation, Dict):
            title_list = recommendation.keys()
            for i in title_list:
                st.subheader(i)
                st.write(recommendation[i])
                trailer_url = get_movie_trailer(i)
                if trailer_url:
                    st.write("Trailer:")
                    st.video(str(trailer_url))
                else:
                    st.write("No trailer found for the movie.")
        else:
            st.write(recommendation)

def get_recommendations(title):
    url = "http://localhost:5000/recommendations"
    params = {'title': title}
    response = requests.get(url, params=params)
    data = response.json()
    return data['recommended_movies']

def get_movie_trailer(title):
    api_key = 'c82aa00d1ffb6ea33249af435464a1fd'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    movie_id = None
    params = {'api_key': api_key, 'query': title}
    response = requests.get(base_url, params=params)
    data = response.json()
    if 'results' in data:
        for result in data['results']:
            if result.get('id'):
                movie_id = result['id']
                break
    if movie_id:
        videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
        params = {'api_key': api_key}
        response = requests.get(videos_url, params=params)
        videos_data = response.json()
        if 'results' in videos_data:
            for video in videos_data['results']:
                if video.get('key'):
                    return f"https://www.youtube.com/watch?v={video['key']}"
    return None



#reccom()
