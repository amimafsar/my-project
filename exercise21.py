'''Name: Amima Afsar
Rollno : 10
List Practical 21

"A teacher stores marks of students in a list

marks = [78, 65, 89, 90, 56]

Write a program to:

Print all marks

Find total marks

Find average marks

Find highest marks

Find lowest marks"'''

marks = [78, 65, 89, 90, 56]
total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
print(f"Marks of students: {marks}")
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks:.2f}")
print(f"Highest marks: {highest_marks}")
print(f"Lowest marks: {lowest_marks}")
