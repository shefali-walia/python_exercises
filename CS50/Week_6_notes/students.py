import csv

students = []

with open("students.csv") as file:
    # for line in file:
    #     name, house = line.rstrip().split(",")
    #     student = {"name": name, "house": house}
    reader = csv.DictReader(file)  # Dictionary reader instead of reader- then we can use column names in csv, can have more data code won't break
    for row in reader:
        students.append(row)

# def get_name(student):
#     return student["name"]
# this function was only used once so we dont need to name it separately, we can use lambda instead- anonymous function

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")