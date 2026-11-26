'''Part - 3: if/elif/else'''
x = 10
if x > 5:
    print("big")
    print("number")
print()
# x = 10
# if x > 5:
#     print("positive")
# print("always runs")     # ← same level as if, if and else should be consucative, the else block should follow its if block that rule is broken here.
# else:
#     print("non-positive")

stock = 8
if stock < 10:
    print("Low stock alert!")
stock = 15                     # modified between the two checks
if not (stock < 10):
    print("Stock is fine.")
print()

stock = 8
if stock < 10:
    print("low stock alert!")
else:
    print("stock is fine.")