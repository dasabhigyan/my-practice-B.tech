# Read three integers n, m, and a representing the dimensions of the square (n x m) and the size of the flagstone (a x a).
# Calculate and print the minimum number of square flagstones needed to pave the entire square, 
# allowing flagstones to extend beyond the square's edge.
# 
# Input Format:
# Three space-separated integers n, m, and a on a single line.
# 
# Output Format:
# A single integer representing the total minimum flagstones needed.


n, m, a = map(int, input().split())

# Calculate how many flagstones fit along each side, rounding up
flagstone_m = (m + a - 1) // a
flagstone_n = (n + a - 1) // a

# Multiply both dimensions to get the total number of flagstones needed
print(flagstone_m * flagstone_n)