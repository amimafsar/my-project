'''Name: Amima Afsar
Rollno : 10
List Practical 8

Given a list of numbers 1-20, create a new list that contains only the even numbers.'''

list_of_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = [num for num in list_of_numbers if num % 2 == 0]
print(even_numbers)