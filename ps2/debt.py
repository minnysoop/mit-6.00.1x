# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

def debt(balance, annualInterestRate, monthlyPaymentRate):
    # Monthly Interest Rate
    monthlyInterestRate = annualInterestRate/12.0
    remaining_balance = balance
    for i in range(0, 12):
        # Find minimum payment
        minimum_payment = remaining_balance * monthlyPaymentRate
        # Calculate unpaid balance
        unpaid_balance = remaining_balance - minimum_payment
        # Calculate interest 
        new_interest = unpaid_balance * monthlyInterestRate
        # Set reminaing balance to the sum of unpaid balance and interest
        remaining_balance = unpaid_balance + new_interest

    print("Remaining balance: ", round(remaining_balance, 2))

def tests():
    debt(42, 0.2, 0.04)
    debt(484, 0.2, 0.04)

tests()