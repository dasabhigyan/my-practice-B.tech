# Read an integer n representing the number for which the factorial needs to be calculated.
# Compute and print the value of n! (n factorial), defined as 1 x 2 x 3 x ... x n, with 0! = 1.
# 
# Input Format:
# A single integer n (0 <= n <= 20).
# 
# Output Format:
# A single integer representing n!.


n = int(input())

# ── Write your solution here ──
i = 1
factorial = 1 
if n == 0:
        print("1")
else:    
        while i <= n:
                factorial = factorial*i
                i += 1
        print(factorial)