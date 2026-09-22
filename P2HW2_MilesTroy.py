# Troy Miles Jr
# 9/22/2026
# P2HW2
# This program may or may not take all entered grades, calculate and display the lowest grade, highest grade, sum of the grades, and the median of the grades

# Enter your grades
module1 = float(input("Enter your grades for module 1: "))
module2 = float(input("Enter your grades for module 2: "))
module3 = float(input("Enter your grades for module 3: "))
module4 = float(input("Enter your grades for module 4: "))
module5 = float(input("Enter your grades for module 5: "))
module6 = float(input("Enter your grades for module 6: "))

# Create a list of the grades
module_grades = [module1, module2, module3, module4, module5, module6]

# Print the list
print(module_grades)

# Sum function for grades
total_grades = sum(module_grades)

# Input for average
median = total_grades / len(module_grades)

# Display total grades
print()
print("--------------------Results---------------------")
print()
print(f"The total value for all the grades is: {total_grades:.2f}")
print()
print(f"The lowest value for the grades is: {min(module_grades)}")
print()
print(f"The highest value for the grades is: {max(module_grades)}")
print()
print(f"The median value for the grades is: {median:.2f}")
print("------------------------------------------------")
# Number of items
print(f"Total number of items in list: {len(module_grades)}")


