import json

student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python",
    "fee": 15000
}

student_json = json.dumps(student)
# print(type(student))
print(student_json)
print(type(student_json))



