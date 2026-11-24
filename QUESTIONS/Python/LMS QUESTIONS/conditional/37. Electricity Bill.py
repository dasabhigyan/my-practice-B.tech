# Read three integers: connection (1 for home, 2 for shop, 3 for factory), units, and is_late (0 or 1).
# Step 1: Calculate bill = units * rate based on connection type and unit slabs:
# - Home (1): <=100 -> rate 3, <=300 -> rate 5, otherwise -> rate 8
# - Shop (2): <=200 -> rate 6, otherwise -> rate 9
# - Factory (3): <=500 -> rate 10, otherwise -> rate 12
# Step 2: If is_late == 1, add a late fee of bill // 10 to the bill amount. Otherwise, add nothing.
# Print two lines: first the bill amount from Step 1, then the final amount to be paid.
connection = int(input()) 
units      = int(input()) 
is_late    = int(input())
bill = 0

if connection == 1:
        if units <= 100:
                bill = units*3
        elif units <= 300:
                bill = units*5
        else:
                bill = units*8

elif connection == 2:
        if units <= 200:
                bill = units*6
        else:
                bill = units*9

elif connection == 3:
        if units <= 500:
                bill = units*10
        else:
                bill = units*12

print(bill)

if is_late == 1:
        a = bill//10
        bill = bill + a
print(bill)
