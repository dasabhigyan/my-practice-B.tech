# Read a single integer units, representing the number of electricity units consumed.
# Calculate the electricity bill using the following progressive slab rates:
# - First 100 units: Rs.3 per unit
# - Next 100 units (101–200): Rs.5 per unit
# - Next 100 units (201–300): Rs.7 per unit
# - Units above 300: Rs.10 per unit
# 
# Input Format:
# One integer units on a single line, representing total electricity units consumed.
# 
# Output Format:
# Print exactly one line containing the total bill in this format:
# Bill: Rs.X.XX (displayed with two decimal places)

units = int(input())
bill = 0 
if units <= 100:
    bill = units*3

elif units <= 200 and units > 100:
    bill = 100*3 + (units - 100)*5

elif units <= 300 and units > 200:
    bill = 100*3 + 100*5 +(units - 200)*7

elif units > 300:
    bill = 100*3 + 100*5 +100*7 + (units - 300)*10

print(f"Bill: Rs.{bill:.2f}")
