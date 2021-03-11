with open(".\letter_templates\letter_1.txt") as file:
    a = file.read()
    print(type(a))
    b=a.replace("[NAME]", "Vibin")
    print(b)