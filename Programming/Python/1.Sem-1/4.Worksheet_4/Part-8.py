print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
'''The expression 0.1 + 0.2 == 0.3 evaluates to false because computers use binary floating-point math, which cannot precisely represent fractional numbers like 0.1 and 0.2, leading to tiny rounding errors'''
print()

print(f"{1/3:.3f}") #0.333 gives the decimal point till 3 points 
print()

print(0.1 + 0.2 == 0.3)            # direct == False
print(round(0.1 + 0.2, 1) == 0.3)  # round first True 
import math
print(math.isclose(0.1 + 0.2, 0.3))  # tolerance-based True 
print()

print(f"{0.1 + 0.2:.1f}")

