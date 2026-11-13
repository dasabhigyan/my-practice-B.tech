'''Part-2 Input,Output, and Beyond the Console'''


# x = input("Enter a number: ") # basic input 
# print(type(x))

# x = input("Enter a number: ")   #this code is trying to string concatenation with an integer, so it was a TypeError
# result = x + 10
# print(result)

# to fix this issue:
x = int(input("Enter a number: "))
result = x + 10
print(result)

# Q17

name = input("Enter your Name:")
year = int(input("Enter your birth year:"))
age = 2026 - year

print(f"Hello {name}! You were born in {year}. You are approxmately {age} years old in 2026")

# Q18 sep and end 

print("Mon", "Tue", "Wed")

print("Mon", "Tue", "Wed", sep=" | ")    #sep sepates the data in the specific data type.

print("Mon", "Tue", "Wed", sep="\n")    # sep = \n make a new line after every value.

print("Loading", end="")     # end with empty string means nothong so no new line 
print("...")

#Q18(c)
print(2026, '06', 26, sep = "/")

#18(d)
print(1 , end = " ")
print(2 , end = " ")
print(3)

#Q19 f-string: format specs 
pi = 3.14159265358979
print(f"raw:    {pi}")
print(f"2 places:{pi:.2f}")
print(f"5 places:{pi:.5f}")     # pi:.5f = means 5 decimal points after the int 

population = 1_400_000_000
print(f"raw:    {population}")
print(f"commans {population:,}")

for name, price in [("Apple",45.5), ("Banana", 12.0), ("Dragonfruit", 310.75)]:
    print(f"{name:<15} Rs. {price:>8.2f}")    
    ''' here <15 means that 15 charaters are fixed for the name but < from the left and in price has reserved 8 charater but the from the right.'''

for n in [1, 12, 123]:
    print(f"Order #{n:04d}")    # 4d means n:>4, but n:04d = replaces empty places with 0 but n:>4.

items = [("Laptop", 1, 75000), ("USB Cable", 3, 499.50)]
print(f"{'Item':<15} {'Qty':>4}   {'Price':>12}")
print("-" * 35)
for name, qty, price in items:
    print(f"{name:<15} {qty:>4}   Rs. {price:>9,.2f}")
'''here in the price the charater are 9 as with 2 decimal included and "," for separation.
7 - 1
5 - 2 
, - 3
0 - 4
0 - 5
0 - 6
. - 7
0 - 8
0 - 9
'''

