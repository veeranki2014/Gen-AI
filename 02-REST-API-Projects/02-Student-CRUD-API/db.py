import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="pydb"
    )

def create_table():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        course VARCHAR(255) NOT NULL,
        fee VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    print("Student Table created successfully")

def create_student(student  ):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "Insert INTO students (Name, course, fee) values (%s, %s, %s)"
    cursor.execute(query, (student.name, student.course, student.fee))

    connection.commit()
    cursor.close()
    connection.close()
    return {
        "Success": True,
        "Message": "Student Table created successfully",
        "data": student
        }

def get_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "select * from students"

    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return {
        "Success": True,
        "Message": "Student data Feteched successfully",
        "data": students
    }

def get_student_by_id(student_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "select * from students where id = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()

    if student:
        return {
            "Success": True,
            "Message": "Student data Feteched successfully",
            "data": student
        }
    else:
        return {
            "Success": False,
            "Message": "Student data Not Found",
            "data": None
        }

def update_student(student_id, student):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "UPDATE students set name = %s, course = %s, fee = %s where id = %s"
    cursor.execute(query, (student.name,student.course, student.fee, student_id))
    connection.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    connection.close()

    if rows_affected > 0:
        return {
            "Success": True,
            "Message": "Student data Feteched successfully",
            "data": student
        }
    else:
        return {
            "Success": False,
            "Message": "Student data Not Found",
            "data": None
        }

def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "DELETE FROM students where id = %s"
    cursor.execute(query, (student_id,))
    connection.commit()

    rows_affected = cursor.rowcount
    cursor.close()
    connection.close()

    if rows_affected > 0:
        return {
            "Success": True,
            "Message": "Student deleted successfully",

        }
    else:
        return {
            "Success": False,
            "Message": "Student Not Found",
            "data": None
        }










