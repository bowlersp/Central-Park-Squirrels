import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Squirrel Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("Squirrel_Totals.csv")
