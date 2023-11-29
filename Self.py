import streamlit as st

# Find more imojis here: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ----HEADER SECTION----
with st.container():  
    st.subheader("Hi, I am Algen Marc :wave:")
    st.title("A Student of BSCPE 1B")
    st.write("I am here to show you the beauty of siargao.")

# ---- WHAT I DO ----
with st.container():
   st.write("---")
   left_column, right_column = st.columns(2)
   with left_column:
      st.header("What I do")
      st.write("##")
      st.write(
         """ 
         
         """
      )
