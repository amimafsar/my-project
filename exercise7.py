'''Name: Amima Afsar
Rollno : 10
List Practical 7

Ask a user for a fruit name. Check if it exists in your fruit_basket list using the in keyword.'''

fruit_basket=["apple","banana","orange","grape","mango"]
fruit_name=input("Enter a fruit name: ")
if fruit_name.lower() in fruit_basket:
    print(f"{fruit_name} exists in the fruit basket.")
else:
    print(f"{fruit_name} does not exist in the fruit basket.")