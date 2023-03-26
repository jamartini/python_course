# with open("weather_data.csv") as wd:
#     content_list = wd.read().splitlines()
# print(content_list)

# import csv
import pandas

# with open("weather_data.csv") as wd:
#     data = csv.reader(wd)
#     data_list = []
#     for line in data:
#         data_list.append(line)
#     temperatures = []
#     for row in data_list:
#         if data_list.index(row) == 0:
#             pass
#         else:
#             temperatures.append(row[2])
# print(temperatures)
# data = pandas.read_csv("weather_data.csv")
# temperatures = data["temp"]
# # temp_list = temperatures.to_list()
# # temp_avr = (sum(temp_list))/(len(temp_list))
# # print(round(data.temp.max()))
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp_f = (monday.temp * 1.8) + 32
# print(monday_temp_f)
data = pandas.read_csv("squirrel_census.csv")
fur_list = data["Primary Fur Color"].to_list()
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count = {
    "colors": ["grey", "cinnamon", "black"],
    "counts": [grey_count, cinnamon_count, black_count]
}

squirrel_df = pandas.DataFrame(squirrel_count)
squirrel_df.to_csv("squirrel_count.csv")
print(squirrel_df)
