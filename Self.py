import streamlit as st

# Find more imojis here: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ----HEADER SECTION----
with st.container():  
    st.subheader("Hi, I am Algen Marc :wave:")
    st.title("A Student of BSCPE 1B")
    st.write("I am here to show you the beauty of siargao.")

# ---- WHAT TO KNOW ----
with st.container():
   st.write("---")
   left_column, right_column = st.columns(2)
   with left_column:
      st.header("What To Know")
      st.write("##")
      st.write(
         """ 
        ABOUT;\n
         -CULTURE & FOOD\n
         -TOP EVENTS & FESTIVALS\n
        THINGS YOU CAN DO IN SIARGAO\n)
         -SURFING\n
         -SUNRISE AND SUNSETS\n
         -ISLAND HOPPING\n
         -SUGBA LAGOON\n
         -CLIFF JUMPING
         -TAYANGBAN CAVE POOLS\n
         -TAKTAK WATERFALL\n
         -BUCAS GRANDE’S LAGOON\n
         -PACIFICO BEACH\n
         -LOCAL COMMUNITY MARKET 
         """
      )
