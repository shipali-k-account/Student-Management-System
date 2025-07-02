from flask import Flask, render_template, request, redirect, url_for, flash
from database import *
from utils import *

app = Flask(__name__)
app.secret_key = 'secret'
create_table()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        roll = request.form['roll']
        name = request.form['name']
        s1 = int(request.form['s1'])
        s2 = int(request.form['s2'])
        s3 = int(request.form['s3'])

        total = calculate_total(s1, s2, s3)
        avg = calculate_average(total)
        grade = calculate_grade(avg)

        insert_student(roll, name, s1, s2, s3, total, avg, grade)
        flash("Student Added Successfully!")
    except Exception as e:
        flash(f"Error: {e}")
    return redirect(url_for('home'))

@app.route('/search', methods=['POST'])
def search():
    roll = request.form['roll']
    student = search_student(roll)
    return render_template('search.html', student=student)

@app.route('/delete', methods=['POST'])
def delete():
    roll = request.form['roll']
    delete_student(roll)
    flash("Student Deleted Successfully!")
    return redirect(url_for('home'))

@app.route('/update_form', methods=['POST'])
def update_form():
    roll = request.form['roll']
    student = search_student(roll)
    if student:
        return render_template('update.html', student=student)
    else:
        flash("Student Not Found")
        return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update():
    roll = request.form['roll']
    name = request.form['name']
    s1 = int(request.form['s1'])
    s2 = int(request.form['s2'])
    s3 = int(request.form['s3'])

    total = calculate_total(s1, s2, s3)
    avg = calculate_average(total)
    grade = calculate_grade(avg)

    update_student(roll, name, s1, s2, s3, total, avg, grade)
    flash("Student Updated Successfully!")
    return redirect(url_for('home'))

@app.route('/display')
def display():
    students = fetch_all()
    return render_template('search.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
