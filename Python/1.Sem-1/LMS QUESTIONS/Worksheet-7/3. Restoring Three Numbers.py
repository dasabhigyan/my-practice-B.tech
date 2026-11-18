# Read three integers b1, b2, and b3 representing the pairwise sums of three original numbers (a1, a2, and a3).
# Recover and print the original numbers a1, a2, and a3 separated by spaces.
# 
# Input Format:
# Three space-separated integers b1, b2, and b3 on a single line.
# 
# Output Format:
# Three space-separated integers a1, a2, and a3 on a single line.




b1, b2, b3 = map(int, input().split())

# ── Write your solution here ──
print(((b1 + b2) - b3)//2, ((b1 + b3) - b2)//2, ((b2 + b3) - b1)//2)