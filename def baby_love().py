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

# Inject CSS for bottom-centered blue button panel
st.markdown("""
    <style>
        .bottom-panel {
            position: fixed;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
            z-index: 9999;
        }
        .macro-button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            transition: background-color 0.3s ease;
        }
        .macro-button:hover {
            background-color: #0056b3;
        }
    </style>
    <div class="bottom-panel">
        <form action="?tab=Dashboard"><button class="macro-button">📊 Dashboard</button></form>
        <form action="?tab=Analytics"><button class="macro-button">📈 Analytics</button></form>
        <form action="?tab=Calculator"><button class="macro-button">🧮 Calculator</button></form>
        <form action="?tab=Data"><button class="macro-button">📁 Data View</button></form>
        <form action="?tab=Settings"><button class="macro-button">⚙️ Settings</button></form>
    </div>
""", unsafe_allow_html=True)

# Read tab from query params
query_params = st.experimental_get_query_params()
if "tab" in query_params:
    st.session_state.active_tab = query_params["tab"][0]

# Main content area
st.markdown(f"<h2 style='color:#007BFF;'>Current Tab: {st.session_state.active_tab}</h2>", unsafe_allow_html=True)

if st.session_state.active_tab == "Dashboard":
    st.write("Welcome to the Dashboard tab.")
elif st.session_state.active_tab == "Analytics":
    st.write("Here are your analytics.")
elif st.session_state.active_tab == "Calculator":
    st.write("Use the calculator here.")
elif st.session_state.active_tab == "Data":
    st.write("Browse your data.")
elif st.session_state.active_tab == "Settings":
    st.write("Adjust your settings.")
else:
    st.write("Choose a tab from the bottom panel.")
