'''Name: Amima Afsar
Rollno : 10
List Practical 11

Take a list like [-5, 3, -2, 8]. Create a new list where all negative numbers are converted to positive.'''

numbers=[-5, 3, -2, 8,-4, 6, 0, -1]
print(numbers)
positive_numbers = [abs(x) for x in numbers]
print(positive_numbers)