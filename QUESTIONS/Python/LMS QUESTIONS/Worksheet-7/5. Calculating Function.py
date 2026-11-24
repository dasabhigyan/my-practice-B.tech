# Read an integer n representing the size of the board / input value.
# The problem calculates an alternating sum sequence where even numbers result in -n // 2
# and odd numbers result in (n + 1) // 2.
# 
# Input Format:
# A single integer n.
# 
# Output Format:
# A single integer representing the result of the calculating function.


n = int(input())

# ── Write your solution here ──
if n % 2 == 0:
    print(-n//2)
else:
    print((n+1)//2)