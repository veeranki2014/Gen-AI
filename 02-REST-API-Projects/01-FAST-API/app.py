
from fastapi import FastAPI, HTTPException
from courses import courses
from pydantic import BaseModel

app = FastAPI()


@app.get("/courses")
def get_courses():
    return courses


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = courses.get(course_id)
    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    return course


@app.get("/courses-search")
def search_course(search: str):
    results = []

    for course_id, course in courses.items():
        if search.lower() in course["course_name"].lower():
            results.append({
                "course_id": course_id,
                **course  ## **Dictionary un packing, will get everything in the dictionary
            })
    return results


### POST Method Example
class Course(BaseModel):
    course_id: int
    course_name: str
    course_price: int


@app.post("/course", status_code=201)
def create_course(course: Course):
    ## Logic to insert data into DB.
    return {
        "message": "Course created successfully",
        course: course
    }
