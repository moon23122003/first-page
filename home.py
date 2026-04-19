import streamlit as st
import time

# Custom CSS for better UI
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: space-around;
    background-color: #4CAF50;
    padding: 10px;
}
.navbar a {
    color: white;
    text-decoration: none;
    font-size: 18px;
}
</style>

<div class="navbar">
    <a href="#">Home</a>
    <a href="#">Sign Up</a>
</div>
""", unsafe_allow_html=True)

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

