
# Troy Miles Jr
# 10/20/2026
# P4HW2 - Employee Payroll
# This program calculates employee pay including overtime, regular pay and gross pay for multiple employees. It also calculates the total amount paid to all employees.
# KIddos, This code WILL NOT WORK. You gotta fix it yourself (press Output)
# Set starting values for payroll totals
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Ask for employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Keep program running until Done is entered
while employee_name != "Done":

    # Ask for hours worked
    hours = float(input(f"How many hours did {employee_name} work? "))

    # Ask for hourly pay rate
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Check if hours exceed 40
    if hours > 40:

        # Calculate overtime hours and pay
        regular_hours = 40
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * pay_rate * 1.5

    # If overtime doesn't apply
    else:
        regular_hours = hours
        overtime_hours = 0
        overtime_pay = 0

    # Calculate regular pay
    regular_pay = regular_hours * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Add employee payroll to running totals
    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_pay
    total_gross_pay = total_gross_pay + gross_pay

    # Count number of employees
    total_employees = total_employees + 1

    # Display payroll information
    print()
    print(f"Employee name: {employee_name}")
    print()
    print(f'{"Hours Worked":<16}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<18}{"RegHour Pay":<18}{"Gross Pay":<15}')
    print("-" * 91)
    print(f'{hours:<16.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:<14.2f}')
    print()

    # Ask for another employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display final payroll totals
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
