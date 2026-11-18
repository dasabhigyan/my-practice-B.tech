# Read an integer n representing the number for which the multiplication table needs to be generated.
# Print the multiplication table of n from 1 to 10.
# Each line must be formatted precisely as: n x i = product
# 
# Input Format:
# A single integer n.
# 
# Output Format:
# Exactly 10 lines containing the multiplication table from 1 to 10.



n = int(input())

# ── Write your solution here ──
i = 1
while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i += 1