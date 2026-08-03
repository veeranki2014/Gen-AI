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
    cursor = connection.cursor()

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
    cursor = connection.cursor()
    query = "Insert INTO students (Name, course, fee) values (%s, %s, %s)"
    cursor.execute(query, (student.name, student.course, student.fee))

    connection.commit()
    cursor.close()
    connection.close()
    return {"Message": "Student Table created successfully"}

def get_students():
    connection = get_connection()
    cursor = connection.cursor()
    query = "select * from students"

    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students

def get_student_by_id(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "select * from students where id = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    return student





