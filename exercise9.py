'''Name: Amima Afsar
Rollno : 10
List Practical 9

Write a program that takes a list of names and a "search_name" from the user. Print the index where the name is found, or "Not Found."'''

list_of_names=["prachi","gargi","arushi","mahek","ananya"]
search_name=input("Enter a name to search: ")
if search_name.lower() in list_of_names:
    index = list_of_names.index(search_name.lower())
    print(f"{search_name} found at index: {index}")
else:
    print("Not Found.")