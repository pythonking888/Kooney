import streamlit as st

# Page config
st.set_page_config(page_title="Macro Buttons", layout="wide")

# Initialize session state for tab control
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Home"

# Inject CSS for dark grey background and blue buttons
st.markdown("""
    <style>
        html, body, .stApp {
            background-color: #2e2e2e !important;
            color: #f0f0f0 !important;
        }
        .block-container {
            background-color: #2e2e2e !important;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #f0f0f0 !important;
        }
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
""", unsafe_allow_html=True)

# Render bottom-centered macro buttons using Streamlit layout
with st.container():
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    with col1:
        if st.button("📊 Dashboard"):
            st.session_state.active_tab = "Dashboard"
    with col2:
        if st.button("📈 Analytics"):
            st.session_state.active_tab = "Analytics"
    with col3:
        if st.button("🧮 Calculator"):
            st.session_state.active_tab = "Calculator"
    with col4:
        if st.button("📁 Data View"):
            st.session_state.active_tab = "Data"
    with col5:
        if st.button("⚙️ Settings"):
            st.session_state.active_tab = "Settings"

# Clean page rendering based on active tab
st.markdown(f"<h2 style='color:#007BFF;'>Current Tab: {st.session_state.active_tab}</h2>", unsafe_allow_html=True)

if st.session_state.active_tab == "Dashboard":
    st.empty()  # Clears previous content
    st.write("🧭 Welcome to the Dashboard.")
elif st.session_state.active_tab == "Analytics":
    st.empty()
    st.write("📈 Analytics tools go here.")
elif st.session_state.active_tab == "Calculator":
    st.empty()
    st.write("🧮 Use the calculator here.")
elif st.session_state.active_tab == "Data":
    st.empty()
    st.write("📁 View your data.")
elif st.session_state.active_tab == "Settings":
    st.empty()
    st.write("⚙️ Adjust your settings.")
else:
    st.empty()
    st.write("Choose a tab from the bottom panel.")
