import streamlit as st
from watchlist import Watchlist
from recs import reccom
from about import about

st.set_page_config(
    page_title="Aniway",
    layout = "centered",
    initial_sidebar_state = "auto"

    )

def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'Recommender','WatchList'])

    if page == 'Home':
        about()
    elif page == 'Recommender':
        reccom()
    elif page == 'WatchList':
        Watchlist()

if __name__ == "__main__":
    main()