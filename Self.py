import requests 
import streamlit as st
from streamlit_lottie import st_lottie

# Find more imojis here: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="Mine Only", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
   r = requests.get(url)
   if r.status_code != 200:\
        return None
   return r.json()
# ---- LOAD ASSETS ----
lottie_coding =  load_lottieurl("https://lottie.host/b3c4efbf-3c67-42b2-ba03-e6e5da2afac5/jXNg2IN9E7.json")
lottie_coding2 = load_lottieurl("https://lottie.host/bc0f39f3-1b10-4569-994f-f867a93306b6/CtcvNKuyXj.json")

# ----HEADER SECTION----
with st.container():  
    st.subheader("Hi, I am Algen Marc a BSCPE student :wave:")
    st.title("SIARGAO")
    st.write("I am here to show you the beauty of SIARGAO.")

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
        THINGS YOU CAN DO IN SIARGAO;\n
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
   with right_column:
      st_lottie(lottie_coding, height=300, key="coding")
      st_lottie(lottie_coding2, height=500, key="coding2")
      
