# with open(file="weather_data.csv", mode="r") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# =======================================================================================
# import csv
#
# with open(file="weather_data.csv", mode="r") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     i = 0
#     for row in data:
#         if i > 0:
#             temp = int(row[1])
#             temperatures.append(temp)
#         i += 1
#     print(temperatures)

# =======================================================================================

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])


