'''Name: Amima Afsar
Rollno : 10
List Practical 22

"Marks of students are stored in a list.

marks = [78, 35, 90, 40, 55]

Write a program to:

Print PASS if marks ≥ 40

Print FAIL if marks < 40

Count how many students passed"'''

marks = [78, 35, 90, 40, 55]
pass_count = 0
for mark in marks:
    if mark >= 40:
        print(f"Marks: {mark} - PASS")
        pass_count += 1
    else:
        print(f"Marks: {mark} - FAIL")
print(f"Total students passed: {pass_count}")
