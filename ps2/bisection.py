# Make this pay.py run faster using a technique introduced in lecture - bisection search!
def bisection(balance, annualInterestRate):

    # Year long payment sequence given a fixed payment
    def calculateBalance(balance, monthlyInterestRate, fixedMonthlyPaymentGuess):
        monthlyUnpaidBalance = balance
        for _ in range(0, 12):
            monthlyUnpaidBalance = monthlyUnpaidBalance - fixedMonthlyPaymentGuess
            monthlyUnpaidBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        return monthlyUnpaidBalance
    
    # Calculate monthly interest rate
    monthlyInterestRate = annualInterestRate / 12.0
    # Define a lower bound
    monthlyPaymentLow = balance / 12.0
    # Define an upper bound
    monthlyPaymentHigh = (balance * (1 + monthlyInterestRate)**12)/12.0

    while True:
        # Make a guess
        fixedMonthlyPaymentGuess = (monthlyPaymentLow + monthlyPaymentHigh)/2.0
        # Threshold
        epsilon = 0.01
        # Find remaining balance given the monthly rate
        remaining_balance = calculateBalance(balance, monthlyInterestRate, fixedMonthlyPaymentGuess)
        # If it's around 0
        if abs(remaining_balance) < epsilon:
            print("Lowest Payment: ", round(fixedMonthlyPaymentGuess, 2))
            break
        # If it's greater than 0
        elif remaining_balance > 0:
            monthlyPaymentLow = fixedMonthlyPaymentGuess
        else:
            monthlyPaymentHigh = fixedMonthlyPaymentGuess

def tests():
    # bisection(3329, 0.2)
    # bisection(4773, 0.2)
    # bisection(3926, 0.2)
    bisection(320000, 0.2)
    bisection(999999, 0.18)

tests()