import csv

data = [
    ["Nombre", "Edad", "Ciudad"],
    ["Pedro", 28, "Madrid"],
    ["Juan", 34, "Barcelona"],
    ["Clara", 22, "Sevilla"]
]

with open("../data/ejemplo.csv", "w", newline="\n", encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
