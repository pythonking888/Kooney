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
import streamlit as st

# Page config
st.set_page_config(page_title="Macro Buttons", layout="wide")

# Initialize session state for tab control
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Home"

# Sidebar-style macro buttons on the right
with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>🔧 Macros</h3>", unsafe_allow_html=True)
    if st.button("📊 Dashboard"):
        st.session_state.active_tab = "Dashboard"
    if st.button("📈 Analytics"):
        st.session_state.active_tab = "Analytics"
    if st.button("🧮 Calculator"):
        st.session_state.active_tab = "Calculator"
    if st.button("📁 Data View"):
        st.session_state.active_tab = "Data View"
    if st.button("⚙️ Settings"):
        st.session_state.active_tab = "Settings"

# Main content area
st.markdown(f"<h2 style='color:#007BFF;'>Current Tab: {st.session_state.active_tab}</h2>", unsafe_allow_html=True)

if st.session_state.active_tab == "Dashboard":
    st.write("Welcome to the Dashboard tab.")
elif st.session_state.active_tab == "Analytics":
    st.write("Here are your analytics.")
elif st.session_state.active_tab == "Calculator":
    st.write("Use the calculator here.")
elif st.session_state.active_tab == "Data View":
    st.write("Browse your data.")
elif st.session_state.active_tab == "Settings":
    st.write("Adjust your settings.")

