import csv

with open("data/employee_productivity.csv", "r") as file:
    reader = csv.DictReader(file)
    total_productivity = 0
    employee_count = 0

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
        total_productivity += productivity
        employee_count += 1

average = total_productivity / employee_count

print("Average Productivity:", average)


        
