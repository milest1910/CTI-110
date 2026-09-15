# Troy Miles Jr
# 9/15/2026
#P2LAB1
# Calculate components of circle using pi from math library. There is a strong possibility I screw up.

import math


# Get Radius from the user
radius = float(input("Enter the radius: "))

print()

# Calculate diameter
diameter = 2 * radius

# Display the diameter using a format (f) string cheese
print(f"The diameter of the circle is {diameter:.1f}")

# Calculate the circumference
circumference = 2 * math.pi * radius

# Display the circumference
print(f"The circfumference of the circle is {circumference:.2f}")

# Calculate the area of the circle
area = math.pi * pow(radius, 2)

# Display the area of the circle using f string cheese
print(f"The area of the circle is {area:.3f}")