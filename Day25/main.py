import pandas

readable = pandas.read_csv("squirrel_count.csv")

total_cinnamon = len(readable[readable["Primary Fur Color"] == "Cinnamon"])
total_gray = len(readable[readable["Primary Fur Color"] == "Gray"])
total_black = len(readable[readable["Primary Fur Color"] == "Black"])

print(total_cinnamon)
print(total_gray)
print(total_black)

data = {
    "Fur Color" : ["Cinnamon", "Gray", "Black"],
    "Count" : [total_cinnamon,total_gray,total_black]
}

dataFrame = pandas.DataFrame(data)

dataFrame.to_csv("squirrel_color_count.csv")