student_dict = {
    "student": ["Vibin", "Febin", "Nathan", "Nolan", "AnuB", "AnuJ"],
    "score": [81, 92, 83, 84, 85, 99]
}

# Looping thru dictionaries
for (key, val) in student_dict.items():
    print(key)
    print(val)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop thru DataFrame
for (key, val) in student_data_frame.items():
    print(key)
    print(val)

#Loop thru rows of DataFrame
for (index, row) in student_data_frame.iterrows():
    #print(row)   #Each of which is a Pandas Series
    print(row.student)
    print(row.score)