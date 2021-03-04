temp_c = {'Monday': 12,
'Tuesday': 14,
'Wednesday': 15,
'Thursday': 14,
'Friday': 21,
'Saturday': 22,
'Sunday': 24
}

temp_f = {day:(t_c*(9/5)+32) for (day,t_c) in temp_c.items()}
print(temp_f)
