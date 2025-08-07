# Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months
def pay(balance, annualInterestRate):
    lowest_payment = 0

    for monthly_fixed_payment in range(0, balance, 10):
        # Calculate monthly interest rate
        monthlyInterestRate = annualInterestRate / 12.0
        # Define remaining balance
        monthlyUnpaidBalance = balance
        # Number of times paid
        times_paid = 0
        while times_paid < 12:
            # Calculate monthly unpaid balance after each payment
            monthlyUnpaidBalance = monthlyUnpaidBalance - monthly_fixed_payment
            # Update times paid
            times_paid += 1
            # Calculate new monthly unpaid balance after interest
            monthlyUnpaidBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        
        # If the monthlyUnpaidBalance reaches 0 before times_paid does
        if monthlyUnpaidBalance <= 0:
            lowest_payment = monthly_fixed_payment
            print("Lowest Payment: ", lowest_payment)
            break

def tests():
    pay(3329, 0.2)
    pay(4773, 0.2)
    pay(3926, 0.2)


tests()