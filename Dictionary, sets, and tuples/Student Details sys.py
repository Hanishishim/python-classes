student = {
    "name": "Hanish",
    "age": 11,
    "marks": 97,
    "address": {
        "city": "Islen",
        "state": "NJ"
    }
}
print(student['name'])
print(student['marks'])
print(student['address']['city'])
student['course'] = 'python'
student['marks'] = 100
print(student)
print(student.items())
