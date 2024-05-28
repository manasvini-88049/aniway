"""
import streamlit as st


st.title("WatchList")
task=st.text_input("enter series")

if "task_list" not in st.session_state:
     st.session_state["task_list"]=[]

if st.button("Add Series  "):
    if task:
        st.session_state["task_list"].append(task)

#if "task_list" not in st.session_state:
     #st.session_state["task_list"]=[]

for i,t in enumerate(st.session_state["task_list"]):
    st.write(f"{i+1}.{t}")

for  i,t in enumerate(st.session_state["task_list"]) :
    if st.checkbox(f"{i+1}.{t}"):
        st.session_state["task_list"].remove(t)
    
  """
import streamlit as st
from streamlit_lottie import st_lottie


def Watchlist():
    st.title("WatchList")
    task = st.text_input("Enter series")

# Retrieve or initialize task_list
    task_list = st.session_state.get("task_list", [])

    if st.button("Add Series"):
        if task:
            task_list.append(task)
            st.session_state["task_list"] = task_list

# Iterate over a copy of the list to avoid modification during iteration
    for i, t in enumerate(task_list.copy()):
    # Display the series with a checkbox
        if st.checkbox(f"{i+1}. {t}"):
        # If the checkbox is checked, remove the series from the list
            task_list.remove(t)
            st.session_state["task_list"] = task_list

# Display the remaining series
    for i, t in enumerate(task_list):
        st.write(f"{i+1}. {t}")

    lottie_url="https://lottie.host/5a39060f-77e5-4225-8d04-2ca1ba862598/7y0lEX1uko.json"
    st_lottie(lottie_url, key="user",height=400)      


   

