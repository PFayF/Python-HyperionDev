"""
This Python program allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator.
In the investment calculator, the user can then enter whether they would like to calculate
the simple interest or the compound interest.
"""

import math

# the user is allowed to choose which calculation they would like to have done
print("\tinvestment - to calculate the amount of interest you'll learn earn on your investment")
print("\tbond       - to calculate the amount you'll have to pay on a home loan")
cal_choice = input("\n\tEnter either 'investment' or 'bond' from the menu above to proceed: ")
cal_choice_lower = cal_choice.lower()

if cal_choice_lower == "investment":            #calculates investment
    original_amount = float(input("\tPlease enter the amount of money you would like to deposit: "))
    interest_rate = float(input("\tPlease enter the interest rate as a percentage (examples 8, 12): "))
    num_of_years = float(input("\tPlease enter the number of years you plan on investing for: "))
    print("\n\tWould you like to calculate simple or compound interest?")
    interest = input("\tPlease enter \"simple\" or \"compound\": ")
    interest = interest.lower()
    interest_rate_divided = interest_rate/100
    if interest == "simple":                    #calculates simple interest
        simple_interest_amount = original_amount * (1 + interest_rate_divided * num_of_years)
        print(f"""\n\tFor the amount you deposited, {original_amount}
        for {num_of_years} years at an interest rate of {interest_rate}%
        by the simple interest calculation, the amount of money 
        you will get back is {round(simple_interest_amount,2)}""")
    elif interest == "compound":                #calculates compound interest
        compound_interest_amount = original_amount * math.pow((1 + interest_rate_divided),num_of_years)
        print(f"""\n\tFor the amount you deposited, {original_amount}
        for {num_of_years} years at an interest rate of {interest_rate}%
        by the compound interest calculation, the amount of money 
        you will get back is {round(compound_interest_amount,2)}""")
    else:
        print(f"\t{interest} is an invalid input.")
elif cal_choice_lower == "bond":                #calculates bond
    present_house_value = float(input("\tPlease enter the present value of the house (example 100000): "))
    interest_rate = float(input("\tPlease enter the interest rate as a percentage (example 7): "))
    num_of_months = float(input("\tPlease enter the number of months you plan to take to repay the bond (example 120): "))
    interest_rate_divided = interest_rate/100
    monthly_interest_rate = interest_rate_divided/12
    repayment = monthly_interest_rate * present_house_value / (1 - math.pow((1 + monthly_interest_rate),-num_of_months))
    print(f"""\n\tFor the present value of the house, {present_house_value}
    \tfor {num_of_months} months at an interest rate of {interest_rate}%
    \tthe amount of money that you will have to repay each month is {round(repayment,2)}""")
else:
    print(f"\t{cal_choice} is an invalid input.")