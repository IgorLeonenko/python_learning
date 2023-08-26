import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color_list = data["Primary Fur Color"].drop_duplicates().to_list()[1::]

count_list = []
for color in fur_color_list:
  count_per_color = len(data[data["Primary Fur Color"] == color])
  count_list.append(count_per_color)

data_dict = {
  "fur color": fur_color_list,
  "count": count_list
}

new_data = pandas.DataFrame(data_dict)

new_data.to_csv("counts_per_color.csv")