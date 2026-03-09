'''Name: Amima Afsar
Rollno : 10
List Practical 15

A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)'''

temp = [35, 45, 55, 65, 75, 85, 95, 25, 30, 40]
count = 0
for t in temp:
    if t > 35:
        count += 1
print(f"Number of hot days: {count}")