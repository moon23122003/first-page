import streamlit as st
import time

# Create horizontal navbar
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"

with col2:
    if st.button("📝 Sign Up"):
        st.session_state.page = "SignUp"

# Default page
if "page" not in st.session_state:
    st.session_state.page = "Home"

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

