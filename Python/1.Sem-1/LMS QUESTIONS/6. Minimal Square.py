# Read two integers, n and k, on a single line.
# Print YES if n is divisible by k, and NO otherwise.
# 
# Input Format:
# Two integers n and k separated by a space.
# 
# Output Format:
# Exactly one line containing either YES or NO.

a, b = map(int, input().split())

# ── Write your solution here ──

if a == 1 and b == 1:
    print(a * 2)
elif a == b:
        print(b)
elif a>b:
        print(a)
elif a<b:
        print(b)

    