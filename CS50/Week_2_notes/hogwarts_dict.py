students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }
#curly braces for dictionaries
for student in students:
    print(student, students[student], sep =", ") 
# student is the key and students[student] is the value (house) associated with that key


"""
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
] 
#none is used for null values in python 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep =", ")
"""