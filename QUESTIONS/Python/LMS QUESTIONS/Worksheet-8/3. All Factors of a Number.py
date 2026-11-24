# Read an integer n representing the number whose factors need to be found.
# Find and print every positive integer that divides n exactly (its factors), in increasing order, one per line.
# 
# Input Format:
# A single integer n.
# 
# Output Format:
# The factors of n, each on a new line, in increasing order.


n = int(input())

# ── Write your solution here ──
i = 1
while i <= n:
        if n%i == 0:
                print(i)
        i += 1
