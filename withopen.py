name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("students.txt", "r+") as file:
    file.write(name + "," + marks + "\n")

print("Student data saved successfully")
