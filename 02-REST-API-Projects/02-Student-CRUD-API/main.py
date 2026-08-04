
from fastapi import FastAPI
from pydantic import BaseModel, Field

import db

app = FastAPI()

API = "/api"  ##F string common URL for all

class Student(BaseModel):
    name: str
    course: str

# Runs once when the application starts.
@app.on_event("startup")
def setup():
    db.create_table()

class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=15)
    course: str = Field(..., min_length=3, max_length=15)
    fee: float  = Field(..., gt=0)

@app.post(f"{API}/student")
def create_student(student: Student):
    return db.create_student(student)

@app.get(f"{API}/students")
def get_all_students():
    return db.get_students()

@app.get(f"{API}/students/{{student_id}}")
def get_student_by_id(student_id: int):
    return db.get_student_by_id(student_id)

@app.put(f"{API}/students/{{student_id}}")
def update_student(student_id: int, student: Student):
    return db.update_student(student_id, student)

@app.delete(f"{API}/students/{{student_id}}")
def delete_student(student_id: int):
    return db.delete_student(student_id)





