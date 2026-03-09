'''Name: Amima Afsar
Rollno : 10
List Practical 12

Calculate the sum of all elements in a list without using the sum() function (use a loop and a tracker variable)'''

numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
total = 0
for n in numbers:
    total += n
print(f"Sum of all elements: {total}")