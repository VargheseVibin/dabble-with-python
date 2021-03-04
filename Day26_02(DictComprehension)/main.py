import random
students = ["Vibin", "Febin", "Nathan", "Nolan", "AnuB", "AnuJ", "Milina", "Noel", "Joel", "JoAnn"]
student_marks = {student:random.randint(0, 100) for student in students}
print(student_marks)

passed_students_mark = {student:student_marks[student] for student in student_marks if student_marks[student] >= 60}
print(passed_students_mark)

passed_students_mark = {student:marks for(student,marks) in student_marks.items() if marks >= 60}
print(passed_students_mark)

