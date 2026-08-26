student = {
    "name": "Hanish",
    "age": 13,
    "marks": 89,
    "address": {
        "city": "Ediosn",
        "state": "NJ"
    }
}
print(student["name"])
print(student["marks"])
print(student["address"]["city"])
student["course"] = "python"
student["marks"] = "97"
print(student.items())
print(student)