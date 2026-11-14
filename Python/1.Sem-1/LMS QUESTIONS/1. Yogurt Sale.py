# Read three integers, one per line: the number of rows (r), columns (c), and a target value (k).
# Count and print how many times the number k appears inside a given r x c grid of integers.
# 
# Input Format:
# - First line: two integers r and c
# - Next r lines: each containing c integers representing the grid rows
# - Last line: an integer k
# 
# Output Format:
# A single integer representing the frequency of k in the grid.



n, a, b = map(int, input().split())

# ── Write your solution here ──
min = 0
pair = 0
single = n*a
pair = b*(n//2) + a*(n%2)

if pair > single:
        print(single)
else:
        print(pair)