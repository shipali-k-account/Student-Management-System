import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS students(
            roll_no TEXT PRIMARY KEY,
            name TEXT,
            subject1 INTEGER,
            subject2 INTEGER,
            subject3 INTEGER,
            total INTEGER,
            average REAL,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_student(roll_no, name, s1, s2, s3, total, avg, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (roll_no, name, s1, s2, s3, total, avg, grade))
    conn.commit()
    conn.close()

def fetch_all():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    conn.close()
    return records

def search_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_student(roll_no, name, s1, s2, s3, total, avg, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, subject1=?, subject2=?, subject3=?, total=?, average=?, grade=?
        WHERE roll_no=?
    """, (name, s1, s2, s3, total, avg, grade, roll_no))
    conn.commit()
    conn.close()

def delete_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()
