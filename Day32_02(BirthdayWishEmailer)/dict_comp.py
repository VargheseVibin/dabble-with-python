import pandas

data = pandas.read_csv("./birthdays.csv")
print(data)
dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(dict)

print(type(dict[(3, 11)]["name"]))
print(dict[(3, 11)]["name"])
