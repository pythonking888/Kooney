import streamlit as st

# Page config
st.set_page_config(page_title="Dark Grey Mode", layout="wide")

# Inject CSS for full dark grey background and light text
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #2e2e2e !important;  /* Dark grey */
            color: #f0f0f0 !important;             /* Light text */
        }
        [data-testid="stVerticalBlock"] {
            background-color: #2e2e2e !important;
        }
        .block-container {
            background-color: #2e2e2e !important;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #f0f0f0 !important;
        }
        .stRadio > div {
            color: #f0f0f0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Minimal content
st.title("🖤 Dark Grey Mode Activated")
st.write("This is your clean, distraction-free layout with a dark grey background.")

col1, col2 = st.columns(2)

with col1:
    st.header("Column A")
    st.write("Content inside Column A")

with col2:
    st.header("Column B")
    st.write("Content inside Column B")
