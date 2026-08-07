import streamlit as st
import api_client

st.title("Student CRUD - Streamlit Consumer")

menu = st.sidebar.selectbox("Action", ["View All", "View by ID", "Add", "Update", "Delete"])

if menu == "View All":
    result = api_client.get_all_students()
    if result.get("Success"):
        st.table(result["data"])
    else:
        st.warning(result.get("Message"))

elif menu == "View by ID":
    student_id = st.number_input("Student ID", min_value=1, step=1)
    if st.button("Fetch"):
        result = api_client.get_student_by_id(student_id)
        if result.get("Success"):
            st.json(result["data"])
        else:
            st.warning(result.get("Message"))

elif menu == "Add":
    name = st.text_input("Name")
    course = st.text_input("Course")
    fee = st.number_input("Fee", min_value=0.0, step=0.01)
    if st.button("Create"):
        result = api_client.create_student(name, course, fee)
        st.success(result.get("Message"))

elif menu == "Update":
    student_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Name")
    course = st.text_input("Course")
    fee = st.number_input("Fee", min_value=0.0, step=0.01)
    if st.button("Update"):
        result = api_client.update_student(student_id, name, course, fee)
        st.success(result.get("Message"))

elif menu == "Delete":
    student_id = st.number_input("Student ID", min_value=1, step=1)
    if st.button("Delete"):
        result = api_client.delete_student(student_id)
        st.success(result.get("Message"))