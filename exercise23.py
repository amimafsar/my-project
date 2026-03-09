'''Name: Amima Afsar
Rollno : 10
List Practical 23

"A cricket player scored runs in 6 matches.
Example: [45, 60, 10, 80, 55, 90]

Write a program to:

Find total runs

Find highest score

Count how many matches player scored more than 50 runs"'''

runs = [45, 60, 10, 80, 55, 90]
total_runs = sum(runs)
highest_score = max(runs)
matches_above_50 = sum(1 for run in runs if run > 50)
print(f"Total runs: {total_runs}")
print(f"Highest score: {highest_score}")
print(f"Matches with more than 50 runs: {matches_above_50}")
