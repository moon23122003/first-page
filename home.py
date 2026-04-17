import streamlit as st
import time

# Page config
st.set_page_config(page_title="My App", page_icon="🚀", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 10em;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "Loading", "Wait"])

# ---------------- HOME ----------------
if page == "Home":
    st.title("🚀 Welcome to My Professional Page")

    name = st.text_input("Enter your name")

    if st.button("Submit"):
        if name:
            st.success(f"Hello, {name}! 👋")
        else:
            st.warning("Please enter your name")

# ---------------- LOADING ----------------
elif page == "Loading":
    st.title("⏳ Loading Demo")

    if st.button("Start Loading"):
        with st.spinner("Loading... please wait"):
            time.sleep(3)
        st.success("Done! ✅")

# ---------------- WAIT ----------------
elif page == "Wait":
    st.title("📊 Processing Demo")

    if st.button("Run Process"):
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

        st.success("Process completed 🎉")
