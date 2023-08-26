# import csv

# data = []
# temperatures = []

# with open("weather_data.csv") as file:
#   rows = csv.reader(file)
#   next(rows)
#   for row in rows:
#     data.append(row)
#     temperatures.append(int(row[1]))

# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()

# average_temp = data.temp.max()

# # print(data[data.temp == average_temp])

# monday = data[data.day == "Monday"]

# print(monday.temp * 9/5 + 32)

data_dict = {
    "students": ['Alan', 'Binan', 'San'],
    "scores": [56, 78, 98]
}

data = pandas.DataFrame(data_dict)

data.to_csv("students.csv")