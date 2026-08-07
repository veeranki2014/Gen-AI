import requests
from config import API_BASE_URL

def get_all_students():
    response = requests.get(f"{API_BASE_URL}/api/students")
    return response.json()

def get_student_by_id(student_id):
    response = requests.get(f"{API_BASE_URL}/api/students/{student_id}")
    return response.json()

def create_student(name, course, fee):
    payload = {"name": name, "course": course, "fee": fee}
    response = requests.post(f"{API_BASE_URL}/api/student", json=payload)
    return response.json()

def update_student(student_id, name, course, fee):
    payload = {"name": name, "course": course, "fee": fee}
    response = requests.put(f"{API_BASE_URL}/api/students/{student_id}", json=payload)
    return response.json()

def delete_student(student_id):
    response = requests.delete(f"{API_BASE_URL}/api/students/{student_id}")
    return response.json()