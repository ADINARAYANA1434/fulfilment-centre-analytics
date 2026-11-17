import csv

with open("data/employee_productivity.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
