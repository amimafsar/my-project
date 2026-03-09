'''Name: Amima Afsar
Rollno : 10
List Practical 13

Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)'''

ages = [15, 22, 17, 30, 12, 25, 18, 5]
minors = [age for age in ages if age < 18]
adults = [age for age in ages if age >= 18]
print("Minors:", minors)
print("Adults:", adults)
