# Troy Miles Jr

# 9/21/2026
# P2LAB2
# Create a dictionary of vehicles and their MPG. Then calculate how many gallons of gas are needed to drive a certain distance. 

# You should place a bet with a friend that this code might not work, just warning you

# Cars and their MPG
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all the vehicle names from the dictionary
keys = car_mpg.keys()

# Display the vehicle names
print(keys)

print()

# Ask thy user which vehicle they want 

vehicle = input("Enter a vehicle to see it's mpg: ")


# Get the mpg for the vehicle entered
mpg = car_mpg[vehicle]

print()

# Display the MPG
print(f"The {vehicle} gets {mpg} mpg.")

print()

# Ask the "so called user" how many miles they will drive
miles = float(input(f"How many miles will you drive the {vehicle}?:"))

# Calculate how many gallons are needed
gallons = miles / mpg

print()

# Display gallons needed rounded to two decimal places
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")