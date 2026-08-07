import streamlit as st

st.title("Student Management")
st.write("This is my first Streamlit app")

st.header("Course details")
st.subheader("Course Details")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
course = st.selectbox("Select Course", ["JAVA", "PHP", "C++", "Python"])
upload_file = st.file_uploader("Choose a file: ", type=["pdf", "docx"])

if st.button("Submit"):
    st.write("Submitting name details:", name)
    st.write("Submitting email details:", email)
    st.write("Submitting course details:", course)
    st.write("Submitting file details:", upload_file)




