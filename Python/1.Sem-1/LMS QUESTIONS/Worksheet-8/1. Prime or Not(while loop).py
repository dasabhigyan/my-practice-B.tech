# Read an integer n (with n >= 1).
# Determine and print whether n is a prime number ("prime" or "not prime").
# A prime number has no divisors other than 1 and itself, and 1 is not considered prime.
# 
# Input Format:
# A single integer n.
# 
# Output Format:
# "prime" if n is prime, or "not prime" otherwise.



n = int(input())

# ── Write your solution here ──

if n <= 1:
    print("not prime")
else:
    is_prime = True
    i = 2
    
    while i < n:
        if n % i == 0:
            is_prime = False
            break  
        i += 1
        
    if is_prime:
        print("prime")
    else:
        print("not prime")
