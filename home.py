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

col1, col2, col3 = st.columns(3)

with col1:
    st.info("💡 Easy to use")

with col2:
    st.success("⚡ Fast Results")

with col3:
    st.warning("🔒 Secure Data")

st.button("Start Diagnosis")

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

