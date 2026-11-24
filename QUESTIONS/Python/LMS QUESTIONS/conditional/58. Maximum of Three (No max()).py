# Read three integers, one per line.
# Find and print the largest of the three values.
# You must determine the largest value using comparisons.
# 
# Do not use:
# - Python's built-in max() function
# - C++'s std::max function
# 
# Input Format:
# Three integers, one per line.
# 
# Output Format:
# Exactly one line containing the largest value.

a = int(input())
b = int(input())
c = int(input())

max = a

if b > a:
        max = b
if c > a:
        max = c 

print(max)