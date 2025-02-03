import pandas

squi = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squi_fur = squi["Primary Fur Color"]
print(squi_fur)
gray = squi[squi_fur == "Gray"]
black = squi[squi_fur == "Black"]
cinnamon = squi[squi_fur == "Cinnamon"]
gray_count = len(gray)
black_count = len(black)
cinnamon_count = len(cinnamon)

squi_dict = {
    "Fur colour": ["gray", "black", "cinnamon"],
    "count": [gray_count, black_count, cinnamon_count]
}
squi_data = pandas.DataFrame(squi_dict)
squi_data.to_csv("new_data.csv")