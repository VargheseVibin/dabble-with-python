import random 

print("Enter the list of Names:")
name_str=input()

names=name_str.split(",")
print(names)
print("Lunch Bill would be paid by:"+names[random.randint(0,(len(names)-1))])