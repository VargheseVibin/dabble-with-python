student_scores = {
    "Vibin" : 82,
    "Febin" : 92,
    "AnuJ" : 98 , 
    "AnuB" : 100,
    "Nathan" : 75,
    "Nolan" : 75 , 
    "NoOne" : 40 , 
}

student_grades = {} 

for student in student_scores:
    if (student_scores[student]) >= 90:
        student_grades[student]="A"
    elif(student_scores[student]) >= 80:
        student_grades[student]="B"
    elif(student_scores[student]) >=70:
        student_grades[student]="C"
    else:
        student_grades[student]="D"

print(student_grades)

