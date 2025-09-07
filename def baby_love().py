import streamlit as st

st.set_page_config(page_title="Hello World", layout="centered")

st.title("👋 Hello, Kamen, !")

st.write("you are my best friend!")
import streamlit as st

# Set page config for dark mode
st.set_page_config(page_title="Leo vs Daddy", layout="centered")

# Inject custom CSS for black background and white text
st.markdown("""
    <style>
        body {
            background-color: black;
            color: white;
        }
        .stApp {
            background-color: black;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p, label {
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
    st.image("https://heroes-and-villain.fandom.com/wiki/Hulk_(Marvel_Cinematic_Universe)", caption="Daddy 💪 (Hulk)")
