# Troy Miles Jr
# October 8, 2026
# P3HW2 - Employee Payroll
# This program might (keyword MIGHT) calculate employee pay, including overtime and gross pay

# Ask for the employee name
employee_name = input("Enter employee's name: ")

# Ask for hours worked
hours = float(input("Enter number of hours worked: "))

# Ask for hourly pay rate
pay_rate = float(input("Enter employee's hourly pay rate: "))

# Check if hours exceed 40
if hours > 40:
    
# If there is overtime, calculate them juicy hours and pay
    regular_hours = 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
# If overtime doesn't apply set OT hours to zero
else:
    regular_hours = hours
    overtime_hours = 0
    overtime_pay = 0

# Calculate regular pay
regular_pay = regular_hours * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display payroll information in columns
print("---------------------------------------------")
print(f"Employee name: {employee_name}")
print()

print(f'{"Hours Worked":<16}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<18}{"RegHour Pay":<18}{"Gross Pay":<15}')
print("-" * 91)
print(f'{hours:<16.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:<14.2f}')

