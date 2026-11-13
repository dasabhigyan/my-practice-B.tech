# Read a single integer n. Check each of the following conditions independently (not as an elif chain) 
# and print the matching tag on its own line for every condition that is true, in this order:
# - If n is positive, print: Positive
# - If n is even, print: Even
# - If n is greater than 100, print: Large
# 
# A number can match one, two, or all three tags.
# If none of the three conditions apply, print None
# 
# Input Format:
# One integer n on a single line.
# 
# Output Format:
# Print one to three lines naming the matching tags (Positive, Even, Large) in that order, 
# or a single line reading None when no tag applies.
n = int(input())
flag = False

if n > 0:
    print("Positive")
    flag = True

if n%2 == 0:
    print("Even")
    flag = True

if n > 100:
    print("Large")
    flag = True

if flag == False:
    print("None")

# Explanation:
# 1. We read an integer 'n'.
# 2. We use a boolean flag (initialized to False) to track if any condition matches.
# 3. We check three independent conditions (Positive, Even, Large) one by one.
# 4. If a condition is met, we print the tag and flip the flag to True.
# 5. At the end, if the flag remains False (meaning no tags matched), we print "None".