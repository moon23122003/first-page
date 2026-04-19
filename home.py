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
    st.title(" welcome to smart diagnosis system ")

    name = st.text_input("Enter your name")

    if st.button("Submit"):
        if name:
            st.success(f"Hello, {name}! 👋")
        else:
            st.warning("Please enter your name")

# ---------------- SIGN UP ----------------
elif page == "sign up":
   import streamlit as st
st.link_button("https://www.hfmmagazine.com/sites/default/files/hfmmagazine/ext/resources/images/2016/October/1116_upfront_microhospital_BSW.jpg")
st.title("SingUp")
name=st.text_input("USER NAME")
password=st.text_input("PASSWORD")
email=st.text_input("Email Id")
age=st.selectbox("Age",1,100)
gender=st.selectbox("GENDER",["M","F","OTHER"])
b1=st.button("SIGNUP")
st.snow()

