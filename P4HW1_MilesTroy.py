
# Troy Miles Jr
# 10/20/2026
# P4HW1
# This program collects grades entered by the user, checks if they are valid, removes the lowest grade, calculates the average of the remaining grades and displays a letter grade.
# WARNING THIS PROGRAM MIGHT NOT WORK. It should be always the case in which I screw up. Idk I'm just here


# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Make sure user enters at least 2 scores
while num_scores < 2:
    print("Please enter at least 2 scores")
    num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list for grades
module_grades = []

# Use a loop to enter grades
for num in range(1, num_scores + 1):
    grade = float(input(f"Enter score #{num}: "))

    # Check if grade is valid
    while grade < 0 or grade > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        grade = float(input(f"Enter score #{num} again: "))

    # Add valid grade to list
    module_grades = module_grades + [grade]

# Find the lowest grade
lowest_grade = min(module_grades)

# Create a new list without the lowest grade
modified_grades = []
lowest_removed = 0

for grade in module_grades:
    if grade == lowest_grade and lowest_removed == 0:
        lowest_removed = 1
    else:
        modified_grades = modified_grades + [grade]

# Calculate average for remaining grades
total_grades = sum(modified_grades)
avg = total_grades / len(modified_grades)

# Determine letter grade for average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print()
print()
print("---------------Results---------------")
print(f"Lowest Score   : {lowest_grade}")
print(f"Modified List  : {modified_grades}")
print(f"Scores Average : {avg:.2f}")
print(f"Grade          : {letter_grade}")
print("-------------------------------------")
