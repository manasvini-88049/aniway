import streamlit as st
from streamlit_lottie import st_lottie
def about():
    st.balloons()
    st.title("Welcome To Aniway!!🦋")   
    st.write("A recommendation system for the animated genre. Whether you love anime or animated movies, worry not, we have got you covered!!Aniway Uses tf idf vector to analyze your prefereance and recommend a series from our database"
    "Further You can use the watchlist to to keep a track of all the series you have watched!!")
    st.write(" TF-IDF (Term Frequency-Inverse Document Frequency) vectorization converts text documents into numerical vectors by assigning weights to each term based on how often they appear in a document and across the entire corpus. This technique captures the importance of terms in documents, enabling tasks like text classification and information retrieval.c")

    st.subheader('Go try Aniway Now')    
     # Example Lottie animation URL 
    #lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
    st.divider()
    lottie_url="https://lottie.host/ae134d07-c6a5-46b1-b623-ef0e30a542fd/SpY2CTELdq.json"
    #lottie_url="https://lottie.host/5a39060f-77e5-4225-8d04-2ca1ba862598/7y0lEX1uko.json"
    st_lottie(lottie_url, key="user",height=400)  
    
