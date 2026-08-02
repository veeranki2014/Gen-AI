import json

student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python",
    "fee": 15000
}

student_json = json.dumps(student, sort_keys=True, indent=4)
# print(type(student))
print(student_json)
print(type(student_json))

print("----------------------------------")
student = json.loads(student_json)
print(type(student))

print("-----------------------------------")

with open("student.json", "w") as f:
    json.dump(student, f, sort_keys=True, indent=4)
    print("JSON file saved Successfully")




