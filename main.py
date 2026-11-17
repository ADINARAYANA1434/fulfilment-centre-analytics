import csv

with open("data/employee_productivity.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        employee = (row["employee"])
        units = int(row["units_processed"])
        hours = int(row["hours_worked"])
        productivity = units / hours
        print(employee)
        print(units)
        print(hours)
        print(productivity)
        print()




        
