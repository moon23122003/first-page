import streamlit as st
st.title("SingUp")
name=st.text_input("USER NAME")
password=st.text_input("PASSWORD")
email=st.text_input("Email Id")
age=st.slider("Age",1,100)
gender=st.selectbox("GENDER",["M","F","OTHER"])
b1=st.button("SIGNUP")
with st.sidebar:
       st.write("Show the above options")
def get_data():
       st.success("Following are the details....")
       st.write(name)
       st.write(password)
       st.write(email)
       st.write(age)
       st.write(gender)
b1=st.button("SIGNUP")
if b1:
       get_data()
