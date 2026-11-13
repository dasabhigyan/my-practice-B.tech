# Read two integers, one per line: x and y, representing the coordinates of a point.
# Determine where the point lies using the following rules:
# 1. If both x and y are 0, print: Origin
# 2. Otherwise, if y is 0 (and x is not 0), print: X-axis
# 3. Otherwise, if x is 0 (and y is not 0), print: Y-axis
# 4. Otherwise, determine the quadrant:
#    - If x > 0 and y > 0, print: Quadrant I
#    - If x < 0 and y > 0, print: Quadrant II
#    - If x < 0 and y < 0, print: Quadrant III
#    - If x > 0 and y < 0, print: Quadrant IV
#
# Input Format:
# Two integers, one per line:
# 1. x
# 2. y
#
# Output Format:
# Exactly one line naming the origin, axis, or quadrant where the point lies.

x = int(input())
y = int(input())

if x == 0 and y == 0:
    print("Origin")

elif y == 0:
    print("X-axis")

elif x == 0:
    print("Y-axis")

elif x > 0 and y > 0:
    print("Quadrant I")

elif x < 0 and y > 0:
    print("Quadrant II")

elif x < 0 and y < 0:
    print("Quadrant III")
    
elif x > 0 and y < 0:
    print("Quadrant IV")