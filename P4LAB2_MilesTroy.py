
# Troy Miles Jr
# 10/20/2026
# P4LAB2
# This program takes an integer and displays the multiplication table from 1 to 12. Negative numbers are not accepted. The user can choose to run the program again.
# As always WARNING!!!!!!!! This program may or MAY NOT work
# Set variable to start the program
run_again = "yes"

# Use while loop to repeat program
while run_again == "yes":

    # Ask user for an integer
    number = int(input("Enter an integer: "))

    print()

    # Check if number is positive or zero
    if number >= 0:

        # Display multiplication table from 1 to 12
        for num in range(1, 13):
            answer = number * num
            print(f"{number} * {num} = {answer}")

    else:
        print("This program does not handle negative numbers")

    print()

    # Ask user if they want to run again
    run_again = input("Would you like to run the program again? ")

    print()

# Exit program
print("Exiting program...")
