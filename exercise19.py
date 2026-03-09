'''Name: Amima Afsar
Rollno : 10
List Practical 19

"A teacher stored attendance of students in a list (1 = present, 0 = absent).
Example: [1,1,0,1,0,1,1]


Write a program to:

Count total present

Count total absent

Print attendance percentage"'''

attendance = [1,1,0,1,0,1,1,0,0,1,1]
total_present = attendance.count(1)
total_absent = attendance.count(0)
attendance_percentage = (total_present / len(attendance)) * 100
print(f"Total present: {total_present}")
print(f"Total absent: {total_absent}")
print(f"Attendance percentage: {attendance_percentage:.2f}%")
