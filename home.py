import streamlit as st
import time
import streamlit as st

st.set_page_config(page_title="Smart Diagnosis System", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size:40px;
        color:#2c3e50;
        text-align:center;
        font-weight:bold;
    }
    .subtitle {
        font-size:20px;
        text-align:center;
        color:gray;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Smart Diagnosis System 🩺</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Get instant health predictions based on symptoms</p>', unsafe_allow_html=True)

#-----------------navigation------------
# Sidebar menu
menu = st.sidebar.selectbox("Choose menu", ["Home", "Loading", "Wait"])
#-----------------home---------------

if menu == "Home":
    st.title("🏠 Home")

elif menu == "sign up":
    st.title("🩺 sign up")

elif menu == "About":
    st.title("ℹ️ about us")
# ---------------- HOME ----------------
if menu == "Home":
    st.title(" welcome to smart diagnosis system ")

    name = st.text_input("Enter your name")

    if st.button("Submit"):
        if name:
            st.success(f"Hello, {name}! 👋")
        else:
            st.warning("Please enter your name")

# ---------------- SIGN UP ----------------
elif menu == "sign up":
   import streamlit as st
st.title("SingUp")
name=st.text_input("USER NAME")
password=st.text_input("PASSWORD")
email=st.text_input("Email Id")
age=st.slider("Age",1,100)
gender=st.selectbox("GENDER",["M","F","OTHER"])
b1=st.button("SIGNUP")
st.snow()

#----------------about----------------

import streamlit as st

st.title("about us")
st.markdown("""here we are to diagnosis in proper way . so the**'color:red' [user can't feel uneasy and also easy to use for any ahe of people]**""")
