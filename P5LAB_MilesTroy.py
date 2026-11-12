# Troy Miles Jr.
# November 12, 2026
# P5LAB
# Simulate a self-checkout and display the bills and coins owed as change.

import random


def disperse_change(change):
    # Convert the change to whole cents before counting denominations.
    cents = round(change * 100)

    # Count each denomination, then subtract its value from the balance.
    dollars = cents // 100
    cents = cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    # The remaining cents are pennies.
    pennies = cents

    # Print only denominations used, with the correct singular or plural.
    if change == 0:
        print("No change")
    else:
        if dollars > 0:
            print(dollars, "Dollar" if dollars == 1 else "Dollars")
        if quarters > 0:
            print(quarters, "Quarter" if quarters == 1 else "Quarters")
        if dimes > 0:
            print(dimes, "Dime" if dimes == 1 else "Dimes")
        if nickels > 0:
            print(nickels, "Nickel" if nickels == 1 else "Nickels")
        if pennies > 0:
            print(pennies, "Penny" if pennies == 1 else "Pennies")


def main():
    # Generate the purchase total and show the amount owed.
    total = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total:.2f}")

    # Ask how much cash the customer will put into the machine.
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Check the payment before calculating and displaying the change.
    if cash < total:
        print(f"Please enter at least ${total:.2f}.")
    else:
        change = round(cash - total, 2)
        print(f"Change is: ${change:.2f}")
        print()
        disperse_change(change)


main()
