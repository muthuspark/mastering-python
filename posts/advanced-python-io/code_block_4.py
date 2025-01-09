import csv

data = [["Name", "Age", "City"], ["John", "30", "New York"], ["Jane", "25", "London"]]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)