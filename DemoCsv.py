import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Rahul", 21, 85])
    writer.writerow(["Anjali", 20, 92])
    writer.writerow(["Kiran", 22, 78])
