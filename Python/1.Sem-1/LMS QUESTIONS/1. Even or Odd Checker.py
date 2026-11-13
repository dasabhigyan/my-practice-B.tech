# Read a single integer (can be negative, zero, or positive).
# If the number is divisible by 2, print "Even".
# Otherwise, print "Odd".
n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")