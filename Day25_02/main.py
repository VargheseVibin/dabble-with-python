import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

avg_temp = data["temp"].mean()
print(f"Average Temp: f{avg_temp}")
max_temp = data["temp"].max()
print(f"Max Temp: {max_temp}")

# Prints Monday row from Data Frame
print(data[data["day"] == "Monday"])

# Prints Row with Max Temp
print(data[data["temp"] == data["temp"].max()])
data[data.temp == data.temp.max()]

# Get Monday's Condition
monday = data[data.day == "Monday"]
print(monday.condition)

# Monday's Temp in F
monday_temp_F = (int(monday.temp) * (9/5) + 32)
print(f"Monday Temp in F: {monday_temp_F}")


student_data = {
    "Name": ["Vibin", "Febin", "Nathan", "Nolan"],
    "scores": [80, 81, 82, 84]
}
df = pandas.DataFrame(student_data)
print(df)
df.to_csv("student_data.csv")



