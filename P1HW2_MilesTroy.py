# Troy Miles Jr
# 9/9/2026
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print()

# Ask user to enter their budget
budget = int(input("Enter Budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")
print()

#Ask user how much they will spend on gas
gas = int(input("How much do you think you will spend on gas? " ))
print()

# Ask how much they will spend on accomodation
accomodation = int(input("Approximately, how much will you need for accomodations/hotel? "))
print()

# Ask user how much they will spend on food
food = int(input("Last, how much do you need for food? "))
print()

# Add all travel expenses TOGETHEERRRRRRRR
expenses = gas + accomodation + food

# Subtract expenses from the starting budget
remaining_balance = budget - expenses

# Display travel expense results
print("------------Travel Expenses-------------")
print("Location", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accomodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)