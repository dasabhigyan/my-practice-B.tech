# Read two integers, m and n, representing the number of rows and columns of a rectangular board.
# Find the maximum number of 2x1 dominoes you can fit on the board without any overlap.
# 
# Input Format:
# Two integers m and n on one line, separated by a space.
# 
# Output Format:
# A single integer representing the maximum number of dominoes.

m, n = map(int, input().split())

# ── Write your solution here ──
total_area = m*n
domino_used = total_area//2
print(domino_used)