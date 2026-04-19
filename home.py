import streamlit as st
import time

st.set_page_config(page_title="Smart Diagnosis", page_icon="🏥", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #ffffff, #e8f5e9);
    }
    .hero {
        background: rgba(255, 255, 255, 0.75);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 30px;
    }
    .hero h1 {
        color: #0f4c75;
        font-size: 48px;
        margin-bottom: 10px;
    }
    .hero p {
        color: #333333;
        font-size: 20px;
    }
    .feature-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
menu = ["Home", "sign up"]
page = st.sidebar.selectbox("Navigation", menu)

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
st.link_button("go to screenshot","hospital")
st.title("SingUp")
name=st.text_input("USER NAME")
password=st.text_input("PASSWORD")
email=st.text_input("Email Id")
age=st.slider("Age",1,100)
gender=st.selectbox("GENDER",["M","F","OTHER"])
b1=st.button("SIGNUP")
st.snow()

