import streamlit as st
from streamlit.components.v1 import html

# Set page config
st.set_page_config(page_title="Leo vs Daddy", layout="centered")

# Inject CSS for full black background and white text
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: black !important;
            color: white !important;
        }
        h1, h2, h3, h4, h5, h6, p, label, .css-1v3fvcr {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title and question
st.title("Who Do You Love More? ❤️")
choice = st.radio("Choose one:", ["Leo", "Daddy"])

# Display image based on choice
if choice == "Leo":
    st.image("https://raisingchildren.net.au/newborns/behaviour/understanding-behaviour/newborn-behaviour", caption="Leo 👶")
elif choice == "Daddy":
    st.image("https://upload.wikimedia.org/wikipedia/en/5/59/Hulk_%28comics_character%29.png", caption="Daddy 💪 (Hulk)")

# Inject fire animation at the bottom using HTML
html("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; height: 200px; z-index: -1; overflow: hidden;">
        <video autoplay muted loop style="width: 100%; height: 100%; object-fit: cover;">
            <source src="https://cdn.pixabay.com/vimeo/769189097/fire-animated-background.mp4?width=1280&hash=4a1e3d4b3f" type="video/mp4">
        </video>
    </div>
""", height=200)
