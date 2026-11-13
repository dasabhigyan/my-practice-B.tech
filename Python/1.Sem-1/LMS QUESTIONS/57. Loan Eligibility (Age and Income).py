# Read two integers, one per line: age and monthly income.
# Check eligibility in the following order:
# 1. If age is below 18, print:
#    Not eligible: age requirement not met.
# 2. Otherwise, if monthly income is below 30000, print:
#    Not eligible: income too low.
# 3. Otherwise, if the applicant is 18 or older and has a monthly income of 30000 or more, print:
#    Loan approved.
# 
# Only one result should be printed.
# 
# Input Format:
# Two integers, one per line:
# 1. age
# 2. monthly income
# 
# Output Format:
# Exactly one line containing the eligibility result.

age = int(input())
income = int(input())

if age < 18:
        print("Not eligible: age requirement not met.")

elif income < 30000:
        print("Not eligible: income too low.")

elif age >= 18 and income >= 30000:
        print("Loan approved.")