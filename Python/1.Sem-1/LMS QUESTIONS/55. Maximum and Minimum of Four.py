# Read four integers, one per line.
# Find and print the largest and smallest values using only comparisons.
# 
# Do not use:
# - Python's built-in max() or min() functions
# - C++'s std::max or std::min functions
# 
# Input Format:
# Four integers, one per line.
# 
# Output Format:
# Print exactly two lines:
# Max: X Min: Y
# where X is the largest value and Y is the smallest value.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

max_val = a

min_val = a

if b > max_val:
    max_val = b
if b < min_val:
    min_val = b

if c > max_val:
    max_val = c
if c < min_val:
    min_val = c

if d > max_val:
    max_val = d
if d < min_val:
    min_val = d

print(f"Max: {max_val}")
print(f"Min: {min_val}")