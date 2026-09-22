# Troy Miles Jr
# 9/21/2026

# P2HW1
# This program should calculate travel expenses and displays the remaining balance after all expenses are subtracted. Might completely fall off the face of the planet

print("This program calculates and displays travel expenses")

print()

# Get the user's budget
budget = float(input("Enter Budget: "))

print()

# Get the travel destination
destination = input("Enter your travel destination: ")

print()

# Get gas expenses
gas = float(input("How much do you think you will spend on gas?: "))

print()

# Get accomodation expenses

accomodation = float(input("Approximately, how much will you need for accomodation/hotel?: "))

print()

# Get food expenses
food = float(input("How much do you need for food?: "))

print()

# Calculate total expenses
expenses = gas + accomodation + food

# Calculate remaining balance
balance = budget - expenses

# Display travel expenses
print("-----------------Travel Expenses-------------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accomodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("--------------------------------------------------")

print()

# Display remaining balance
print(f"{'Remaining Balance:':<20}${balance:.2f}")