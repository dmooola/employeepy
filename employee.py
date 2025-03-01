'''
This is a program that will ask the use to enter their name, hours worked, and rate as an employee. It has parameters that won't allow an employee to enter negative hours or an hourly rate less than $14. The program will then print the employee name, gross pay, taxed income, and net income. The user has the option to repeat the process again
'''

# Return False if hours worked is a negative number
def validateHours(hoursWorked):
    if hoursWorked < 0:
        return False
    return True

# Return False if the rate per hour is less than $14.00
def validateRate(rate):
    if rate < 14.00:
        return False
    return True

# Calculate and return the regular payment
def straighTime(rate, hours):
    if hours <= 40:
        return rate * hours
    else:
        return rate * 40

# Calculate and return the extra payment
def timeandaHalf(rate, hours):
    if hours <= 40:
        return 0
    else:
        return (hours - 40) * (rate * 1.5)

# Calculate and return the tax payment
def taxAmount(payment, taxRate):
    return payment * taxRate / 100

# Driver program
def main():
    tax_rate = 7
    while True:
        full_name = input("Enter your employee full name (or type 'exit' to quit): ")
        if full_name.lower() == 'exit':
            break

        hours_worked = float(input("Enter hours worked: "))
        if not validateHours(hours_worked):
            print("Please enter a non-negative number.")
            continue

        rate_per_hour = float(input("Enter rate per hour: "))
        if not validateRate(rate_per_hour):
            print("Rate should be at least $14.00.")
            continue

        regular_payment = straighTime(rate_per_hour, hours_worked)
        overtime_payment = timeandaHalf(rate_per_hour, hours_worked)
        gross_pay = regular_payment + overtime_payment
        tax_amount = taxAmount(gross_pay, tax_rate)
        net_pay = gross_pay - tax_amount

        print("\nEmployee Name:", full_name)
        print("Gross Pay:", "${:.2f}".format(gross_pay))
        print("Tax Amount ({}%):".format(tax_rate), "${:.2f}".format(tax_amount))
        print("Net Pay:", "${:.2f}".format(net_pay))
        print("")

if __name__ == "__main__":
    main()
