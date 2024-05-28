
import streamlit as st
import requests
import time
from typing import Dict

st.set_page_config(
    page_title="Aniway",
    layout = "centered",
    initial_sidebar_state = "auto"

    )
#page_bg_img = f"""
#<style>
#[data-testid="stAppViewContainer"] > .main {{
#background-color:#E8F9FF;
#background-position: top left;
#background-repeat: no-repeat;
#background-attachment: local;
#}}
#.st-emotion-cache-6qob1r
#{{
    #background-color:black;
#}}


#[data-testid="stHeader"] {{
#background: black;
#}}

#[data-testid="stToolbar"] {{
#right: 2rem;
#}}
#</style>
#"""
# Display the custom HTML
#st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.header("Welcome to Aniway🐼",anchor='',divider='red')
st.sidebar.image(image="images/naruto.jpeg" ,use_column_width=True)
st.snow()
# Streamlit app
def main():
    st.title("Aniway: An animation Recommendation System 🦋🐼")
    st.subheader('',divider='red')
    st.header("Aniway: For All things animation!")
    st.divider()
    title_input = st.text_input("Enter an anime title:")
    if st.button("Suggest!!"):
        #recommendations = get_recommendations(title_input)
        recommendation = get_recommendations(title_input)
        st.write("Recommended Movies:")
        #for movie in recommendations:
            #st.write(movie)
        if isinstance(recommendation, Dict):    
            title_list=recommendation.keys()
            for i in title_list:
                st.write(i)
                st.write(recommendation[i])
                #posters = get_movie_posters(i)
                trailer_url = get_movie_trailer(i)
        # Display posters
                #if posters:
    #st.header("Movie Posters")
    #for title, poster_url in posters.items():
                    #st.subheader(i)
                    #st.image(posters, caption=i, use_column_width="auto",width=20)
                #else:
                    #st.write("No posters found for the entered movie titles.")
                if trailer_url:
                  st.write("Trailer:") #trailer_url)  # Display the URL for debugging
                  st.video(str(trailer_url))
                else:
                 st.write("No trailer found for the movie.")

        else:
             st.write(recommendation)        


    
 
    
# Function to make API request to Flask endpoint                  

def get_recommendations(title):
    url = "http://localhost:5000/recommendations"
    params = {'title': title}
    response = requests.get(url, params=params)
    data = response.json()
    return data['recommended_movies']

#def get_movie_posters(title):
    #api_key = 'c82aa00d1ffb6ea33249af435464a1fd'
    #base_url = 'https://api.themoviedb.org/3/search/movie'
    #posters = {}

    #for title in movie_titles:
        # Make request to TMDb API
    #params = {'api_key': api_key, 'query': title}
    #response = requests.get(base_url, params=params)
    #data = response.json()

        # Extract poster path if available
    #if 'results' in data:
        #for result in data['results']:
            #if result.get('poster_path'):
                #return f"https://image.tmdb.org/t/p/w500/{result['poster_path']}"

    # If no poster found, return None
    #return None    




def get_movie_trailer(title):
    api_key = 'c82aa00d1ffb6ea33249af435464a1fd'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    movie_id=None
    # Make request to TMDb API
    params = {'api_key': api_key, 'query': title}
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract movie ID if available
    if 'results' in data:
        for result in data['results']:
            if result.get('id'):
                movie_id = result['id']
                break
    
    # If movie ID found, make request to get videos
    if movie_id:
        videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
        params = {'api_key': api_key}
        response = requests.get(videos_url, params=params)
        videos_data = response.json()
        
        # Extract video key if available
        if 'results' in videos_data:
            for video in videos_data['results']:
                if video.get('key'):
                    return f"https://www.youtube.com/watch?v={video['key']}"
    
    # If no video found, return None
    return None


   
       
if __name__ == "__main__":
    main()

    


