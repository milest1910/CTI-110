# Troy Miles Jr
# 9/9/2026 
# P1HW1
# This program may or may not calculate exponents and perfeorm addition and subtraction. It highly depends on how good I code this.

print("-----Calculating Exponents-----")
print()

# Get base and exponent from user
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent:"))
print()

# Calculate exponent
answer = base ** exponent

# Display exponent result
print(base, "raised to the power of", exponent, "is", answer, "!!")
print()

print("-----Addition and Subtraction-----")
print()

# Get them integers from the USERRRRRRRRRRR
starting_number = int(input("Enter a starting integer: "))
add_number = int(input("Enter an integer to add: "))
subtract_number = int(input("Enter an integer to subtract: "))
print()

# Calculate answer
final_answer = starting_number + add_number - subtract_number

# Display answer
print(starting_number, "+", add_number, "-", subtract_number, "is equal to", final_answer)
