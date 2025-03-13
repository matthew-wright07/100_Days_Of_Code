import pandas

data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]
print(monday.temp*1.8+32)