'''Name: Amima Afsar
Rollno : 10
List Practical 10

Given a list of 10 student marks, count how many students scored above 40.'''
marks = [35, 45, 55, 65, 75, 85, 95, 25, 30, 40]
count = 0
for mark in marks:
    if mark > 40:
        count += 1
print(f"Number of students who scored above 40: {count}")